# Health Tracker API Documentation


 ### Introduction
 
The basis of this project is to empower users to perform a more in-depth analysis of their health metrics. Comprehensive analysis of health metrics will enable individuals to make more health-conscious decisions, leading to better physical longevity and mental health. The end goal of this project is to use a suite of apps from which to extract data physical, mental, and nutritional metrics and perform cross correlative analysis in each of these categories. Hopefully, utilizing the Health Tracker API, we can make insightful conclusions regarding an individual's health status leading to better preventative care and overall well-being.

---
### Dictionary

The dictionary illustrated below contains key-value pairs of the following biometrics extracted from the Apple Health App. The intention behind this dictionary is to map concise naming conventions to Apple's naming convention type. The dictionary will make sense shortly when using the more concise naming conventions as arguments in our functions.The following table also contains a description column giving a brief description of the biometric and a link containing either a white paper or article from a reputuable instritution (***Eventually all links will be replaced with peer reviewed publications***).

Dictionart Key Chart
| Key      |Key Value Health Metrics| Description |
| ----------- | ----------- | ----------- |
| HeartRate      | HKQuantityTypeIdentifierHeartRate       | Heart rate is the speed of the heartbeat measured by the number of contractions of the heart per minute. [Harvard Health Rate](https://www.health.harvard.edu/heart-health/what-your-heart-rate-is-telling-you)|
| StepCount   | HKQuantityTypeIdentifierStepCount        | Number of flights per day. [Number of Steps](https://www.nih.gov/news-events/nih-research-matters/number-steps-day-more-important-step-intensity)|
|WalkingDistance|HKQuantityTypeIdentifierDistanceWalkingRunning| Total distace traveled in a day. [Walking and Running Health](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4067492/)|
|BasalEnergyBurned|HKQuantityTypeIdentifierBasalEnergyBurned| Your BMR (Basal Metabolic Rate) is an estimate of how many calories your body burns at rest. It represents the minimum amount of energy needed to keep your body functioning, including breathing and keeping your heart beating. [Basal Metabolic Rate](https://www.sciencedirect.com/topics/medicine-and-dentistry/basal-metabolic-rate)  |
|FlightsOfStairs|HKQuantityTypeIdentifierFlightsClimbed| Numebr of flights of stairs per day.  |
|ExerciseTime|HKQuantityTypeIdentifierAppleExerciseTime| Total amount of exercise time in a given day.|
|RestingHeartRate|HKQuantityTypeIdentifierRestingHeartRate| |
|V02Max|HKQuantityTypeIdentifierVO2Max| |
|WalkingHRAvg|HKQuantityTypeIdentifierWalkingHeartRateAverage| |
|AudioLevels|HKQuantityTypeIdentifierHeadphoneAudioExposure| |
|WalkingDoubleSupport|HKQuantityTypeIdentifierWalkingDoubleSupportPercentage| |
|SixMinWalkingDist|HKQuantityTypeIdentifierSixMinuteWalkTestDistance| |
|StandTime|HKQuantityTypeIdentifierAppleStandTime| |
|WalkingSpeed|HKQuantityTypeIdentifierWalkingSpeed| |
|WalkingStepLength|HKQuantityTypeIdentifierWalkingStepLength| |
|WalkingAsymmetry|HKQuantityTypeIdentifierWalkingAsymmetryPercentage| |
|SleepingGoal|HKDataTypeSleepDurationGoal| |
|SleepAnalysis|HKCategoryTypeIdentifierSleepAnalysis| |
|StandHour|HKCategoryTypeIdentifierAppleStandHour| |
|Meditation|HKCategoryTypeIdentifierMindfulSession| |
|HighHeartRate|HKCategoryTypeIdentifierHighHeartRateEvent| |
|LowHeartRate|HKCategoryTypeIdentifierLowHeartRateEvent| |
|HeartRateVarSDNN|HKQuantityTypeIdentifierHeartRateVariabilitySDNN| |
