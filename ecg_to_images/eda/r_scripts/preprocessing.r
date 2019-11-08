install.packages("RHRV", repos="http://R-Forge.R-project.org")
library('RHRV')

setwd("/home/george/Data/RR intervals/shareedb/RRouts-test-r-script")
files <- list.files(path = "/home/george/Data/RR intervals/shareedb/RRouts-test-r-script",
                    pattern = "*.txt",
                    full.names = TRUE,
                    recursive = FALSE)  

lst <- vector("list", length(files))
names(lst) <- files
# pct.vector <- vector("list", length(files))

pct.vector <- numeric(length(files))
start.time <- Sys.time()

low_values <- 0
high_values <- 0

for (i in 1:length(files)){
    hrv.data  = CreateHRVData()
    hrv.data = SetVerbose(hrv.data, TRUE )
    
    fullFileName <- files[i]
    # fullFileName <- "/home/george/Data/RR intervals/shareedb/RRouts-test-r-script/rr02062.txt"
    
    hrv.data = LoadBeatRR(hrv.data, 
                          files[i],
                          RecordPath=".",
                          scale = 1, 
                          datetime = "1/1/1900 0:0:0",
                          verbose = NULL)
    
    hrv.data = BuildNIHR(hrv.data)
    
    # PlotNIHR(hrv.data, Tags = NULL, Indexes = NULL,
    #          main = "Non-interpolated instantaneous heart rate", xlab = "time (sec.)",
    #          ylab = "HR (beats/min.)", type = "l", ylim = NULL, Tag = NULL,
    #          verbose = NULL)
    
    hrv.data.filtered = FilterNIHR(hrv.data)
    
    rr.intervals <- hrv.data$Beat$Time

    rr.intervals.discarded <- length(hrv.data$Beat$Time) - length(hrv.data.filtered$Beat$Time) 
    rr.intervals.filtered <- length(hrv.data.filtered$Beat$Time)
    
    # Find percentage of filtered data
    rr.intervals.filtered.pct <- (rr.intervals.filtered * 100)  / length(rr.intervals)
    pct.vector[i] <- rr.intervals.filtered.pct
    
    if (pct.vector[i] < 80){
        low_values <- low_values + 1
    } else {
        high_values <- high_values + 1 
    }
     
    rr.hr <- hrv.data$Beat$niHR
    rr.mV <- hrv.data$Beat$RR
    
    write.table(rr.intervals, file = paste("./filtered_data/output-Intervals.txt", basename(fullFileName), sep = ""), sep = "\t",
                row.names=FALSE, col.names=FALSE)
    
    write.table(rr.hr, file = paste("./filtered_data/output-HeartRate.txt", basename(fullFileName), sep = ""), sep = "\t",
                row.names=FALSE, col.names=FALSE)
    
    write.table(rr.mV, file=paste("./filtered_data/output-milliVolt.txt", basename(fullFileName), sep = ""), sep = "\t",
                row.names=FALSE, col.names=FALSE)
}

result.min = min(pct.vector, na.rm=TRUE)
result.max = max(pct.vector, na.rm=TRUE)
result.mean = mean(pct.vector, na.rm=TRUE)
result.median = median(pct.vector, na.rm=TRUE)

end.time <- Sys.time()
end.time - start.time
                    
