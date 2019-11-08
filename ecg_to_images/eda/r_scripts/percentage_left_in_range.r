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

for (i in 1:length(files)){

  fullFileName <- files[i]
  rr.intervals <- scan(fullFileName)
  rr.range <- rr.intervals[rr.intervals >=0.6 & rr.intervals <= 1.2]
  
  # Find percentage of filtered data
  rr.intervals.range.pct <- (length(rr.range) * 100)  / length(rr.intervals)
  print(rr.intervals.range.pct)
  pct.vector[i] <- rr.intervals.range.pct
  
  if (pct.vector[i] < 80){
    low_values <- low_values + 1
  } else {
    high_values <- high_values + 1 
  }
}

result.min = min(pct.vector, na.rm=TRUE)
result.max = max(pct.vector, na.rm=TRUE)
result.mean = mean(pct.vector, na.rm=TRUE)
result.median = median(pct.vector, na.rm=TRUE)

end.time <- Sys.time()
end.time - start.time

