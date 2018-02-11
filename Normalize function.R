normalize <- function(x){
  (x-mean(x))/sd(x)
}