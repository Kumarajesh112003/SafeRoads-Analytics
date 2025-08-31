# -*- coding: utf-8 -*-


if(!require(party)) install.packages("party", dependencies=TRUE)

library(party)

dataset <- read.csv("Data_Final.csv")

dataset$Severity_Class <- ifelse(dataset$SEVERITY >= 2, "HIGH", "MODERATE")

input.dat <- dataset[1:10000,]

output.tree <- ctree(Severity_Class ~ DAY_OF_WEEK + LIGHT_CONDITION + ALCOHOLTIME + SPEED_ZONE, data = input.dat)

png(file = "decision_tree_accidents.png", width=800, height=600)
plot(output.tree, main="Decision Tree for Accident Severity")
dev.off()

print("Decision Tree saved as decision_tree_accidents.png")
