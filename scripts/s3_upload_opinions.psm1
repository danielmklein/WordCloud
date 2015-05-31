Import-Module AWSPowerShell;

$opinion_dir = "C:\Users\Daniel\Dropbox\Class_Files\CBH_301\Word_Cloud\supreme_court_opinions\test_output\opinions";
$opinion_bucket_name = "scotus-opinions";

function Upload-Opinions ()
{
	Get-ChildItem $opinion_dir -Filter *.txt | %{
		$opinion_path = Join-Path $opinion_dir $_;
		#$opinion_path | write-host;

		"Uploading {0} to S3 bucket {1}" -f $opinion_path,$opinion_bucket_name | write-host;
		Write-S3Object -BucketName $opinion_bucket_name -File $opinion_path;

	}
}