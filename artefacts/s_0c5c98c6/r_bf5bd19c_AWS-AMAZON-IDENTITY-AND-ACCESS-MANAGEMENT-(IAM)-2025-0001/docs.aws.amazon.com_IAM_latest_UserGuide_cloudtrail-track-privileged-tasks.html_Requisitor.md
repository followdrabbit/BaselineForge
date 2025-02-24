```json
[
  {
    "Description": "Ensure `AssumeRoot` sessions are tracked in CloudTrail logs by identifying the `AssumeRoot` event in the `eventName` field.",
    "Reference": "Track privileged tasks in AWS CloudTrail section - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html",
    "Observations": "The event should be monitored to detect any unauthorized root-level actions in the account."
  },
  {
    "Description": "Identify the `targetPrincipal` and `accessKeyId` fields in CloudTrail logs to determine which member account actions were taken on and the unique session credentials used.",
    "Reference": "Track privileged tasks in AWS CloudTrail section - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html",
    "Observations": "These fields help correlate actions taken in the `AssumeRoot` session with the specific resources and accounts affected."
  },
  {
    "Description": "Search CloudTrail logs for the `accessKeyId` from the `AssumeRoot` event to find all privileged tasks performed during the session.",
    "Reference": "Track privileged tasks in AWS CloudTrail section - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html",
    "Observations": "The privileged tasks performed can be identified by the `eventName` field values in the logs corresponding to the session."
  },
  {
    "Description": "Verify that the maximum session duration for `AssumeRoot` is limited to 900 seconds (15 minutes).",
    "Reference": "Track privileged tasks in AWS CloudTrail section - URL: https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html",
    "Observations": "Short session durations help limit the exposure of root credentials."
  }
]
```