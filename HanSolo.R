#!/usr/bin/env Rscript

# --------------------------------------------------------
# Author: Vanja Börjesson
# Date: 2017-02-09
# This script plots the GC frequency over several sequences
# --------------------------------------------------------
rm(list=ls())

# Control that there is three arguments
arg <- commandArgs(trailingOnly=TRUE)
if (length(arg)!=3) {
  stop("Three argument must be supplied; input1.csv input2.csv output", call.=FALSE)
}

#install.packages("ggplot2")
library(ggplot2)
library(data.table)

# read in csv-files 
gc <- fread(arg[1])
info <- fread(arg[2])

# Calculate number of ids and windows 
nr_id <- ncol(gc)
nr_wind <- nrow(gc)

# Create an x-axis and y-axis
gc$length <- 1:nr_wind

library(tidyr)
library(ggplot2)

gc_plotdata <- gather(gc, "length", 'ID', 1:nr_id)
names(gc_plotdata) <- c("length", 'ID', "PercentageGC")

# install.packages("viridis")
library(viridis)
p <- ggplot(gc_plotdata, aes(ID, length)) +
  geom_raster(aes(fill=PercentageGC)) + coord_flip() + 
  scale_fill_gradientn(colours = viridis(256))+
#  scale_fill_gradient(low = "white", high = "darkblue") +
  theme_minimal()
p

#### plot data table ######

library(gridExtra)
names(info) <- c("Ids", 'Length', 'GC frequence')
info

# Set theme to table
t_grey <- ttheme_default(colhead=list(fg_params = list(parse=TRUE)))
tbl <- tableGrob(info, 
                 rows=NULL, 
                 theme=t_grey)

# Plot chart and table into one object
grid.arrange(p, tbl,
             as.table=TRUE)

#### Save and print plot to pdf ####

user_name = arg[3]
ggsave(paste0(user_name, '.pdf'))
