data <- read.csv("comparison_scores.csv")
plot(density(data$GAN.Comparison.Score), col = "blue", lwd = 1, xlim = c(0, 1.2), ylim = c(0, 8), main = "Comparison Scores", xlab = "Similarity Scores", ylab = "Density")
lines(density(data$Non.Mated.Comparison.Score), col = "red", lwd = 1)
lines(density(data$Mated.Comparison.Score), col = "green", lwd = 1)

legend("topleft", legend = c("GAN", "Non-Mated", "Mated"), col = c("blue", "red", "green"), lwd = 1)
