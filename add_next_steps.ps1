
# Adds/replaces "## Next Step" links for C++ content files
# Handles: 00. Headers/Fundamentals, 00. Headers/Others, 01. Basics,
#          02. Basic Problems (Search, Sorting), 03-06 folders, Algorithms

$base = "c:\Users\Rohaj Jaiswal\OneDrive\Desktop\DSA\1. C++"
$changed = 0

function Get-FriendlyName($filename) {
    # Strip numbering prefix and .md, make human readable
    $name = [System.IO.Path]::GetFileNameWithoutExtension($filename)
    $name = $name -replace '^\d+_', ''
    $name = $name -replace '_', ' '
    return $name
}

function Add-NextStep($filePath, $nextFilePath, $nextFileName) {
    $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    $friendly = Get-FriendlyName($nextFileName)

    # Build the Next Step block
    $nextBlock = "`n---`n`n## Next Step`n`n- Go to [$nextFileName]($nextFileName) to continue with $friendly.`n"

    # Remove any existing Next Step / 🚀 Next Steps sections to the end of file
    # Pattern: everything from ## Next Step or ## 🚀 Next Steps to end of file
    $cleaned = $content -replace '(?ms)\r?\n---\r?\n\r?\n## (Next Step|🚀 Next Steps).*$', ''
    $cleaned = $cleaned -replace '(?ms)\r?\n## (Next Step|🚀 Next Steps).*$', ''

    # Also remove trailing metadata blocks (dashes, bold lines at end of Fundamentals files)
    # like  ---\n**Examples...\n**Key Functions...\n**Common Use Cases...\n
    $cleaned = $cleaned -replace '(?ms)\r?\n---\r?\n\r?\n\*\*Examples.*$', ''

    # Trim trailing whitespace
    $cleaned = $cleaned.TrimEnd()

    $newContent = $cleaned + $nextBlock

    if ($content -ne $newContent) {
        [System.IO.File]::WriteAllText($filePath, $newContent, [System.Text.Encoding]::UTF8)
        $script:changed++
        Write-Host "Updated: $(Split-Path $filePath -Leaf)"
    }
}

function Add-NextStepToChain($folder, $files, $finalTarget, $finalTargetName) {
    # $files = ordered list of non-README .md files
    # $finalTarget = relative path that the last file should point to
    # $finalTargetName = display name for the final link
    for ($i = 0; $i -lt $files.Count; $i++) {
        $currentFile = $files[$i]
        if ($i -lt $files.Count - 1) {
            $nextFile = $files[$i + 1]
            $nextName = Split-Path $nextFile -Leaf
            Add-NextStep $currentFile $nextName $nextName
        } else {
            # Last file points to final target
            $lastContent = [System.IO.File]::ReadAllText($currentFile, [System.Text.Encoding]::UTF8)
            $nextBlock = "`n---`n`n## Next Step`n`n- Go to [$finalTargetName]($finalTarget) to continue.`n"
            $cleaned = $lastContent -replace '(?ms)\r?\n---\r?\n\r?\n## (Next Step|🚀 Next Steps).*$', ''
            $cleaned = $cleaned -replace '(?ms)\r?\n## (Next Step|🚀 Next Steps).*$', ''
            $cleaned = $cleaned -replace '(?ms)\r?\n---\r?\n\r?\n\*\*Examples.*$', ''
            $cleaned = $cleaned.TrimEnd()
            $newContent = $cleaned + $nextBlock
            if ($lastContent -ne $newContent) {
                [System.IO.File]::WriteAllText($currentFile, $newContent, [System.Text.Encoding]::UTF8)
                $script:changed++
                Write-Host "Updated (last): $(Split-Path $currentFile -Leaf) → $finalTargetName"
            }
        }
    }
}

# === 00. Headers and Libraries / Fundamentals ===
$fundFolder = "$base\00. Headers and Libraries\Fundamentals"
$fundFiles = Get-ChildItem -Path $fundFolder -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
Add-NextStepToChain $fundFolder $fundFiles "README.md" "README.md"

# === 00. Headers and Libraries / Others ===
$othersFolder = "$base\00. Headers and Libraries\Others"
$othersFiles = Get-ChildItem -Path $othersFolder -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
Add-NextStepToChain $othersFolder $othersFiles "README.md" "README.md"

# === 01. Basics ===
$basicsFolder = "$base\01. Basics"
$basicsFiles = Get-ChildItem -Path $basicsFolder -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
Add-NextStepToChain $basicsFolder $basicsFiles "README.md" "README.md"

# === 02. Basic Problems / Search ===
$searchFolder = "$base\02. Basic Problems\Search"
$searchFiles = Get-ChildItem -Path $searchFolder -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
Add-NextStepToChain $searchFolder $searchFiles "README.md" "README.md"

# === 02. Basic Problems / Sorting ===
$sortFolder = "$base\02. Basic Problems\Sorting"
$sortFiles = Get-ChildItem -Path $sortFolder -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
Add-NextStepToChain $sortFolder $sortFiles "README.md" "README.md"

# === 03. OOPS - process each sub-folder ===
$oopsRoot = "$base\03. OOPS"
$oopsSubFolders = Get-ChildItem -Path $oopsRoot -Directory | Sort-Object Name
foreach ($subDir in $oopsSubFolders) {
    $subFiles = Get-ChildItem -Path $subDir.FullName -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
    if ($subFiles.Count -gt 0) {
        Add-NextStepToChain $subDir.FullName $subFiles "README.md" "README.md"
    }
    # Also check for sub-sub-folders
    $subSubFolders = Get-ChildItem -Path $subDir.FullName -Directory | Sort-Object Name
    foreach ($subSub in $subSubFolders) {
        $ssFiles = Get-ChildItem -Path $subSub.FullName -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
        if ($ssFiles.Count -gt 0) {
            Add-NextStepToChain $subSub.FullName $ssFiles "README.md" "README.md"
        }
    }
}

# === 04. Data Structures ===
$dsFolder = "$base\04. Data Structures"
$dsFiles = Get-ChildItem -Path $dsFolder -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
Add-NextStepToChain $dsFolder $dsFiles "README.md" "README.md"

# === 05. Trees and Graphs - process each sub-folder ===
$tgRoot = "$base\05. Trees and Graphs"
$tgSubFolders = Get-ChildItem -Path $tgRoot -Directory | Sort-Object Name
foreach ($subDir in $tgSubFolders) {
    $subFiles = Get-ChildItem -Path $subDir.FullName -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
    if ($subFiles.Count -gt 0) {
        Add-NextStepToChain $subDir.FullName $subFiles "README.md" "README.md"
    }
}

# === 06. Problem Solving - process each sub-folder ===
$psRoot = "$base\06. Problem Solving"
$psSubFolders = Get-ChildItem -Path $psRoot -Directory | Sort-Object Name
foreach ($subDir in $psSubFolders) {
    $subFiles = Get-ChildItem -Path $subDir.FullName -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
    if ($subFiles.Count -gt 0) {
        Add-NextStepToChain $subDir.FullName $subFiles "README.md" "README.md"
    }
}

# === Algorithms - process each sub-folder ===
$algRoot = "$base\Algorithms"
$algSubFolders = Get-ChildItem -Path $algRoot -Directory | Sort-Object Name
foreach ($subDir in $algSubFolders) {
    $subFiles = Get-ChildItem -Path $subDir.FullName -Filter "*.md" | Where-Object { $_.Name -ne "README.md" } | Sort-Object Name | Select-Object -ExpandProperty FullName
    if ($subFiles.Count -gt 0) {
        Add-NextStepToChain $subDir.FullName $subFiles "README.md" "README.md"
    }
}

Write-Host ""
Write-Host "=== DONE: Updated $changed C++ content files with Next Step links ==="
