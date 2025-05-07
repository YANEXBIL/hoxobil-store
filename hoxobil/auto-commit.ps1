while ($true) {
    try {
        cd "C:\Users\yanex\OneDrive\Desktop\hoxobil-store"  # Change this path if needed

        git add .

        $time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $commitMessage = "Auto commit at $time"

        git commit -m "$commitMessage" 2>$null

        if ($LASTEXITCODE -eq 0) {
            git push origin main  # Replace 'main' with your branch name if different
            Write-Host "✅ Committed & pushed at $time"
        } else {
            Write-Host "⚠️ Nothing new to commit at $time"
        }

    } catch {
        Write-Host "❌ Error: $($_.Exception.Message)"
    }

    Start-Sleep -Seconds 30  # Wait 30 seconds
}
