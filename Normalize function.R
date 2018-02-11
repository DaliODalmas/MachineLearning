#This function normalizes vectors passed to it 
normalize <- function(x){
  (x-mean(x))/sd(x)
}
