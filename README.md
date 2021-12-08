# Health Tracker API Documentation


 ### Introduction
 
The basis of this project is to empower users to perform a more in-depth analysis of their health metrics. Comprehensive analysis of health metrics will enable individuals to make more health-conscious decisions, leading to better physical longevity and mental health. The end goal of this project is to use a suite of apps from which to extract data physical, mental, and nutritional metrics and perform cross correlative analysis in each of these categories. Hopefully, utilizing the Health Tracker API, we can make insightful conclusions regarding an individual's health status leading to better preventative care and overall well-being.

---

### Getting Setup

#### Exporting Apple Health Data
1. Locate the Health App on iPhone and click on the app.
  <img src="https://user-images.githubusercontent.com/51255104/145128321-472a6b81-9350-4890-b174-970bdd088d74.png" width="250" height='450' title="hover text">
2. Go to the top right corner of the app and click on your profile then scroll to the bottom and click on export all health data.
  <img src="https://user-images.githubusercontent.com/51255104/145130473-5bcf1fb7-f3f2-402f-9f11-50b820bb1f2a.jpg" width="250" height='550' title="hover text">
3. After a few minutes you will be prompted with several methods to export the health data. If you have a mac book I would suggest AirDroping the file otherwise you can send it through e-mail (depending on the file size).
  <img src="https://user-images.githubusercontent.com/51255104/145130501-7c123336-d754-41cf-af91-a28670d573d0.jpg" width="250" height='550' title="hover text">





---
### Dictionary

The dictionary illustrated below contains key-value pairs of the following biometrics extracted from the Apple Health App. The intention behind this dictionary is to map concise naming conventions to Apple's naming convention type. The dictionary will make sense shortly when using the more concise naming conventions as arguments in our functions. The following table also contains a description column giving a brief description of the biometric and a link containing either a white paper or article from a reputuable instritution (***Eventually all links will be replaced with peer reviewed publications***).

Dictionart Key Chart
| Key      |Key Value Health Metrics| Description |
| ----------- | ----------- | ----------- |
| HeartRate      | HKQuantityTypeIdentifierHeartRate       | Heart rate is the speed of the heartbeat measured by the number of contractions of the heart per minute. [Heart Rate](https://www.health.harvard.edu/heart-health/what-your-heart-rate-is-telling-you)|
| StepCount   | HKQuantityTypeIdentifierStepCount        | Number of flights per day. [Number of Steps](https://www.nih.gov/news-events/nih-research-matters/number-steps-day-more-important-step-intensity)|
|WalkingDistance|HKQuantityTypeIdentifierDistanceWalkingRunning| Total distace traveled in a day. [Walking and Running Health](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4067492/)|
|BasalEnergyBurned|HKQuantityTypeIdentifierBasalEnergyBurned| Your BMR (Basal Metabolic Rate) is an estimate of how many calories your body burns at rest. It represents the minimum amount of energy needed to keep your body functioning, including breathing and keeping your heart beating. [Basal Metabolic Rate](https://www.sciencedirect.com/topics/medicine-and-dentistry/basal-metabolic-rate)  |
|FlightsOfStairs|HKQuantityTypeIdentifierFlightsClimbed| Numebr of flights of stairs per day. [Flights of Stairs](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627027/) |
|ExerciseTime|HKQuantityTypeIdentifierAppleExerciseTime| Total amount of exercise time in a given day. [Exercise Duration and Intensity](https://link.springer.com/article/10.1186/1479-5868-7-7)|
|RestingHeartRate|HKQuantityTypeIdentifierRestingHeartRate|A quantity sample type that measures the user’s resting heart rate. [Resting Heart Rate](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0227709)|
|V02Max|HKQuantityTypeIdentifierVO2Max| VO2 max measures how much oxygen (usually in milliliters) you breathe in while exercising as hard as you can. [V02 Max](https://blog.nasm.org/sports-performance/the-value-of-vo2-health-measure-or-performance-marker)|
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

Note: The following dictionary is likely not all encompassing and therefore incomplete. 
