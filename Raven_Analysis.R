library(tidyverse)
library(quanteda)
reddit_data <- read.csv("data_dumps/data_01-14-2022.csv")
posts_data <- reddit_data %>% select(post_name) %>% unique() 
posts_data %>% view()
    
# Word cloud
# set.seed(100)
# textplot_wordcloud(my_dfm, min_count = 6, random_order = FALSE,
#                    rotation = .25, 
#                    colors = RColorBrewer::brewer.pal(8,"Dark2"))