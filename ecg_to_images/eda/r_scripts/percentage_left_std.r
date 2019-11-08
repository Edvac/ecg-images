install.packages("RHRV", repos="http://R-Forge.R-project.org")
install.packages("dplyr")
library('RHRV')
library(dplyr)

setwd("/home/george/Data/RR intervals/shareedb/RRouts-test-r-script")
files <- list.files(path = ".",
                    pattern = "*.txt",
                    full.names = TRUE,
                    recursive = FALSE)  

pct.vector <- numeric(length(files))
start.time <- Sys.time()

low_values <- 0
high_values <- 0

max.value <- 0
min.value <- 100
  
for (i in 1:length(files)){
  
  fullFileName <- files[i]
  # fullFileName <- "/home/george/Data/RR intervals/shareedb/RRouts-test-r-script/rr02062.txt"
  rr.intervals <- scan(fullFileName)
  
  rr.mean <- mean(rr.intervals, na.rm = TRUE)
  rr.std <- sd(rr.intervals, na.rm = TRUE)
  
  rr.result <- vector()
  for (v in rr.intervals){
    if (v < rr.mean){
      if (v > (rr.mean - (2*rr.std))){
      rr.result <- c(rr.result, v)
      }
    } else if (v >= rr.mean){
      if (v < rr.mean + (2*rr.std))
      rr.result <- c(rr.result, v)
    }
  }
  
  # Find percentage of filtered data
  # rr.intervals.result.pct <- (length(rr.result) * 100)  / length(rr.intervals)
  # print(rr.intervals.result.pct)
  # # pct.vector <- rr.intervals.result.pct
  # pct.vector[i] <- rr.intervals.result.pct
  # 
  # if (pct.vector[i] < 80){
  # #if (pct.vector < 80){
  #   low_values <- low_values + 1
  # } else {
  #   high_values <- high_values + 1 
  # }
  if (max.value < max(rr.result, na.rm = TRUE)){
    max.value <- max(rr.result, na.rm = TRUE)
  }
  if (min.value > min(rr.result, na.rm = TRUE))
  min.value <- min(rr.result, na.rm = TRUE)
}
  
result.min = min(pct.vector, na.rm=TRUE)
result.max = max(pct.vector, na.rm=TRUE)
result.mean = mean(pct.vector, na.rm=TRUE)
result.median = median(pct.vector, na.rm=TRUE)

end.time <- Sys.time()
end.time - start.time

