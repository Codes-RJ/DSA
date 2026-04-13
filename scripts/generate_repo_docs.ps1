$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location $repoRoot

function Normalize-LinkPath {
    param([string]$Path)
    return ($Path -replace '\\', '/')
}

function Get-TopicName {
    param([string]$Name)
    $base = if ($Name.EndsWith('.md')) {
        [System.IO.Path]::GetFileNameWithoutExtension($Name)
    } else {
        [System.IO.Path]::GetFileName($Name)
    }
    $base = $base -replace '^[0-9]+[._ ]*', ''
    $base = $base -replace '[_-]+', ' '
    $base = $base -replace '\s+', ' '
    return $base.Trim()
}

function Get-TitleFromFile {
    param([string]$FilePath)
    if ([System.IO.Path]::GetFileName($FilePath) -eq 'README.md') {
        return (Get-TopicName (Split-Path (Split-Path $FilePath -Parent) -Leaf))
    }

    if (-not (Test-Path $FilePath)) {
        return (Get-TopicName ([System.IO.Path]::GetFileName($FilePath)))
    }

    $lines = Get-Content $FilePath
    foreach ($line in $lines) {
        if ($line -match '^#\s+(.+)$') {
            return $Matches[1].Trim()
        }
    }

    return (Get-TopicName ([System.IO.Path]::GetFileName($FilePath)))
}

function Get-RelativePath {
    param(
        [string]$FromDirectory,
        [string]$ToPath
    )

    $fromUri = [System.Uri]((Resolve-Path $FromDirectory).Path + [System.IO.Path]::DirectorySeparatorChar)
    $toUri = [System.Uri](Resolve-Path $ToPath).Path
    return Normalize-LinkPath($fromUri.MakeRelativeUri($toUri).ToString())
}

function Get-Description {
    param(
        [string]$TargetName,
        [bool]$IsDirectory
    )

    $topic = Get-TopicName $TargetName
    if ($IsDirectory) {
        return "continue with the $topic section"
    }

    return "understand $topic"
}

function Ensure-Directory {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        New-Item -ItemType Directory -Path $Path | Out-Null
    }
}

function New-PlaceholderFile {
    param(
        [string]$FilePath,
        [string]$LanguageName
    )

    if (Test-Path $FilePath) {
        return
    }

    $name = [System.IO.Path]::GetFileName($FilePath)
    $topic = if ($name -eq 'README.md') {
        Get-TopicName (Split-Path (Split-Path $FilePath -Parent) -Leaf)
    } else {
        Get-TopicName $name
    }
    $title = "# $topic"
    $body = @(
        $title,
        "",
        "This file mirrors the C++ repository structure for $LanguageName.",
        "",
        "Content for this topic can be expanded here while keeping naming and traversal aligned across languages."
    ) -join "`n"

    Set-Content -Path $FilePath -Value $body -Encoding UTF8
}

function Normalize-PlaceholderHeading {
    param(
        [string]$ReadmePath,
        [string]$DirectoryPath
    )

    $content = Get-Content -Raw $ReadmePath
    if ([string]::IsNullOrWhiteSpace($content)) {
        return
    }

    $expectedTitle = "# $(Get-TopicName (Split-Path $DirectoryPath -Leaf))"
    $regex = [regex]'(?m)^#(?:\s*| README)\s*$'
    $updated = $regex.Replace(
        $content,
        [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $expectedTitle },
        1
    )

    if ($updated -ne $content) {
        Set-Content -Path $ReadmePath -Value $updated.TrimEnd() -Encoding UTF8
    }
}

function Upsert-GeneratedBlock {
    param(
        [string]$Content,
        [string]$StartMarker,
        [string]$EndMarker,
        [string]$Block
    )

    $escapedStart = [regex]::Escape($StartMarker)
    $escapedEnd = [regex]::Escape($EndMarker)
    $pattern = "(?s)$escapedStart.*?$escapedEnd\r?\n?"
    $replacement = $Block.TrimEnd() + "`n"

    if ($Content -match [regex]::Escape($StartMarker)) {
        return [regex]::Replace($Content, $pattern, $replacement)
    }

    return $replacement + "`n" + $Content.TrimStart()
}

function Remove-GeneratedNextStep {
    param([string]$Content)

    $startMarker = '<!-- AUTO-GENERATED NEXT STEP START -->'
    $endMarker = '<!-- AUTO-GENERATED NEXT STEP END -->'
    $escapedStart = [regex]::Escape($startMarker)
    $escapedEnd = [regex]::Escape($endMarker)
    $pattern = "(?s)$escapedStart.*?$escapedEnd\r?\n?"
    return [regex]::Replace($Content, $pattern, '').TrimEnd()
}

function Set-ReadmeNavigation {
    param(
        [string]$DirectoryPath,
        [string]$ReadmePath,
        [bool]$IsRoot = $false
    )

    Ensure-Directory $DirectoryPath
    if (-not (Test-Path $ReadmePath)) {
        $folderName = Split-Path $DirectoryPath -Leaf
        $initial = @(
            "# $(Get-TopicName $folderName)",
            "",
            "This README is the navigation index for this folder."
        ) -join "`n"
        Set-Content -Path $ReadmePath -Value $initial -Encoding UTF8
    }

    Normalize-PlaceholderHeading -ReadmePath $ReadmePath -DirectoryPath $DirectoryPath

    $items = Get-ChildItem $DirectoryPath | Sort-Object { -not $_.PSIsContainer }, Name
    $rows = New-Object System.Collections.Generic.List[string]
    $flowNodes = New-Object System.Collections.Generic.List[string]
    $nodeRefs = @()
    $counter = 1

    foreach ($item in $items) {
        if ($item.Name -eq 'README.md' -and -not $IsRoot) {
            continue
        }

        if (-not $item.PSIsContainer -and $item.Extension -ne '.md') {
            continue
        }

        if ($item.PSIsContainer) {
            $target = Join-Path $item.FullName 'README.md'
            if (-not (Test-Path $target)) {
                $folderTitle = "# $(Get-TopicName $item.Name)"
                Set-Content -Path $target -Value ($folderTitle + "`n`nThis README is the navigation index for this folder.") -Encoding UTF8
            }
            $linkPath = Get-RelativePath $DirectoryPath $target
            $description = Get-Description $item.Name $true
            $rows.Add("| Folder | [$($item.Name)]($linkPath) | $description |")
            $nodeLabel = $item.Name -replace '"', "'"
            $flowNodes.Add("    N$counter[`"$nodeLabel`"]")
            $nodeRefs += "N$counter"
        } else {
            $linkPath = Get-RelativePath $DirectoryPath $item.FullName
            $description = Get-Description $item.Name $false
            $rows.Add("| File | [$($item.Name)]($linkPath) | $description |")
            $nodeLabel = $item.Name -replace '"', "'"
            $flowNodes.Add("    N$counter[`"$nodeLabel`"]")
            $nodeRefs += "N$counter"
        }

        $counter++
    }

    if ($rows.Count -eq 0) {
        $rows.Add("| Info | This folder is currently being expanded. | Additional files will be added here. |")
        $flowNodes.Add('    N1["Folder expansion in progress"]')
        $nodeRefs += 'N1'
    }

    $flowEdges = New-Object System.Collections.Generic.List[string]
    for ($i = 0; $i -lt ($nodeRefs.Count - 1); $i++) {
        $flowEdges.Add("    $($nodeRefs[$i]) --> $($nodeRefs[$i + 1])")
    }

    $startMarker = '<!-- AUTO-GENERATED NAV START -->'
    $endMarker = '<!-- AUTO-GENERATED NAV END -->'
    $rowsText = [string]::Join("`n", $rows)
    $flowNodesText = [string]::Join("`n", $flowNodes)
    $flowEdgesText = [string]::Join("`n", $flowEdges)

    $block = @(
        $startMarker,
        "## Folder Map",
        "",
        "| Type | Name | Purpose |",
        "| --- | --- | --- |",
        $rowsText,
        "",
        "## Flowchart",
        "",
        '```mermaid',
        'flowchart TD',
        $flowNodesText,
        $flowEdgesText,
        '```',
        $endMarker
    ) -join "`n"

    $content = Get-Content -Raw $ReadmePath
    $updated = Upsert-GeneratedBlock -Content $content -StartMarker $startMarker -EndMarker $endMarker -Block $block
    Set-Content -Path $ReadmePath -Value $updated.TrimEnd() -Encoding UTF8
}

function Get-MarkdownTraversal {
    param(
        [string[]]$Roots,
        [string[]]$ExcludedRootFiles
    )

    $all = New-Object System.Collections.Generic.List[string]

    function Add-DirectoryMarkdown {
        param(
            [string]$DirectoryPath,
            [System.Collections.Generic.List[string]]$Accumulator
        )

        $readmePath = Join-Path $DirectoryPath 'README.md'
        if (Test-Path $readmePath) {
            $Accumulator.Add((Resolve-Path $readmePath).Path)
        }

        $files = Get-ChildItem $DirectoryPath -File -Filter '*.md' |
            Where-Object { $_.Name -ne 'README.md' } |
            Sort-Object Name
        foreach ($file in $files) {
            $Accumulator.Add($file.FullName)
        }

        $directories = Get-ChildItem $DirectoryPath -Directory | Sort-Object Name
        foreach ($directory in $directories) {
            Add-DirectoryMarkdown -DirectoryPath $directory.FullName -Accumulator $Accumulator
        }
    }

    foreach ($root in $Roots) {
        $fullRoot = (Resolve-Path $root).Path
        Add-DirectoryMarkdown -DirectoryPath $fullRoot -Accumulator $all
    }

    $unique = $all | Select-Object -Unique
    return $unique | Where-Object {
        $relative = $_.Replace($repoRoot + '\', '')
        $ExcludedRootFiles -notcontains $relative
    }
}

function Set-NextStepBlocks {
    param([string[]]$Traversal)

    $startMarker = '<!-- AUTO-GENERATED NEXT STEP START -->'
    $endMarker = '<!-- AUTO-GENERATED NEXT STEP END -->'

    for ($i = 0; $i -lt $Traversal.Count; $i++) {
        $file = $Traversal[$i]
        $nextFile = if ($i + 1 -lt $Traversal.Count) { $Traversal[$i + 1] } else { (Join-Path $repoRoot 'README.md') }
        $content = Get-Content -Raw $file
        $clean = Remove-GeneratedNextStep $content

        $linkPath = Get-RelativePath (Split-Path $file -Parent) $nextFile
        $targetName = [System.IO.Path]::GetFileName($nextFile)
        $targetTitle = Get-TitleFromFile $nextFile
        $description = ($targetTitle -replace '^#+\s*', '')
        $block = @(
            $startMarker,
            "## Next Step",
            "",
            "- Go to [$targetName]($linkPath) to understand $description.",
            $endMarker
        ) -join "`n"
        $updated = $clean.TrimEnd() + "`n`n" + $block + "`n"

        Set-Content -Path $file -Value $updated.TrimEnd() -Encoding UTF8
    }
}

function Mirror-CppStructure {
    param(
        [string]$SourceRoot,
        [string]$TargetRoot,
        [string]$LanguageName
    )

    $sourceBase = (Resolve-Path $SourceRoot).Path
    Ensure-Directory $TargetRoot

    Get-ChildItem -Recurse -Directory $SourceRoot | ForEach-Object {
        $relative = $_.FullName.Substring($sourceBase.Length).TrimStart('\')
        $targetDir = Join-Path $TargetRoot $relative
        Ensure-Directory $targetDir
    }

    Get-ChildItem -Recurse -File $SourceRoot -Filter '*.md' | ForEach-Object {
        $relative = $_.FullName.Substring($sourceBase.Length).TrimStart('\')
        $targetFile = Join-Path $TargetRoot $relative
        Ensure-Directory (Split-Path $targetFile -Parent)
        New-PlaceholderFile -FilePath $targetFile -LanguageName $LanguageName
    }
}

function Ensure-MkDocsPages {
    $docsRoot = Join-Path $repoRoot 'docs\docs'
    $required = @(
        'getting-started/installation.md',
        'getting-started/quick-start.md',
        'getting-started/environment.md',
        'basics/learning-basics.md',
        'basics/variables.md',
        'basics/control-flow.md',
        'basics/functions.md',
        'basics/arrays-strings.md',
        'data-structures/linear/arrays.md',
        'data-structures/linear/linked-lists.md',
        'data-structures/linear/stacks.md',
        'data-structures/linear/queues.md',
        'data-structures/non-linear/trees.md',
        'data-structures/non-linear/graphs.md',
        'data-structures/non-linear/heaps.md',
        'data-structures/non-linear/tries.md',
        'data-structures/advanced/segment-trees.md',
        'data-structures/advanced/fenwick-trees.md',
        'data-structures/advanced/dsu.md',
        'algorithms/searching.md',
        'algorithms/sorting.md',
        'algorithms/recursion.md',
        'algorithms/dynamic-programming.md',
        'algorithms/greedy.md',
        'algorithms/graph-algorithms.md',
        'algorithms/advanced.md',
        'practice/patterns.md',
        'practice/interview.md',
        'practice/problem-solving.md',
        'resources/study-plans.md',
        'resources/templates.md',
        'resources/references.md',
        'contributing/guidelines.md',
        'contributing/code-style.md',
        'contributing/documentation.md'
    )

    foreach ($relative in $required) {
        $path = Join-Path $docsRoot $relative
        Ensure-Directory (Split-Path $path -Parent)
        if (-not (Test-Path $path)) {
            $topic = Get-TopicName ([System.IO.Path]::GetFileName($path))
            $body = @(
                "# $topic",
                "",
                "This documentation page was added to match the configured MkDocs navigation.",
                "",
                "It can be expanded with repository-specific detail as the documentation grows."
            ) -join "`n"
            Set-Content -Path $path -Value $body -Encoding UTF8
        }
    }
}

$excludedRootFiles = @(
    'README.md',
    'LICENSE',
    'CODE_OF_CONDUCT.md',
    'CONTRIBUTING.md',
    'SECURITY.md',
    'CHANGES_TO_BE_MADE.md'
)

Mirror-CppStructure -SourceRoot '1. C++' -TargetRoot '2. Java' -LanguageName 'Java'
Mirror-CppStructure -SourceRoot '1. C++' -TargetRoot '3. Python' -LanguageName 'Python'
Ensure-MkDocsPages

$readmeDirectories = @(
    $repoRoot
    (Join-Path $repoRoot '1. C++')
    (Join-Path $repoRoot '2. Java')
    (Join-Path $repoRoot '3. Python')
)

$readmeDirectories += (Get-ChildItem -Recurse -Directory '1. C++' | ForEach-Object { $_.FullName })
$readmeDirectories += (Get-ChildItem -Recurse -Directory '2. Java' | ForEach-Object { $_.FullName })
$readmeDirectories += (Get-ChildItem -Recurse -Directory '3. Python' | ForEach-Object { $_.FullName })
$readmeDirectories = $readmeDirectories | Select-Object -Unique

foreach ($dir in $readmeDirectories) {
    $readme = Join-Path $dir 'README.md'
    $isRoot = $dir -eq $repoRoot
    Set-ReadmeNavigation -DirectoryPath $dir -ReadmePath $readme -IsRoot:$isRoot
}

$docsDirectories = (Get-ChildItem -Recurse -Directory 'docs\docs').FullName
foreach ($dir in $docsDirectories) {
    $readme = Join-Path $dir 'README.md'
    Set-ReadmeNavigation -DirectoryPath $dir -ReadmePath $readme
}

$traversalRoots = @('.github', '1. C++', '2. Java', '3. Python', 'docs', 'scripts')
$traversal = Get-MarkdownTraversal -Roots $traversalRoots -ExcludedRootFiles $excludedRootFiles
Set-NextStepBlocks -Traversal $traversal
