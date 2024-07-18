## 1. Prepare
### 1.1 Installing Packages

install.packages("rlang")

install.packages("ggplot2")

install.packages("scales")

install.packages("readxl")

install.packages("xlsx")

install.packages("tidyr")

install.packages("dplyr")

install.packages("forcats")

install.packages("reshape2")

install.packages("viridis")

install.packages("stringr")

library(ggplot2) #data visualization

library(scales) #data transformation

library(readxl) #read Excel files

library(xlsx) #Excel I/O operations

library(tidyr) #data wrangling

library(dplyr) #data manipulation

library(forcats) #categorical data operations

library(reshape2) #data reshaping

library(viridis) #color palettes

library(stringr) #string manipulation
```

df <- read.csv("../input/social-media-impact-on-mental-health-in-india/df.csv")
df2 <- read.csv("../input/social-media-impact-on-mental-health-in-india/df2.csv")
df3 <- read.csv("../input/social-media-impact-on-mental-health-in-india/df3.csv")
df4 <- read.csv("../input/social-media-impact-on-mental-health-in-india/df4.csv")
df5 <- read.csv("../input/social-media-impact-on-mental-health-in-india/df5.csv")
df6 <- read.csv("../input/social-media-impact-on-mental-health-in-india/df6.csv")
df7 <- read.csv("../input/social-media-impact-on-mental-health-in-india/df7.csv")
df_long <- read.csv("../input/social-media-impact-on-mental-health-in-india/df_long.csv")
df_sorted <- read.csv("../input/social-media-impact-on-mental-health-in-india/df_sorted.csv")
avg_time_spent_worldwide <- read.csv("../input/social-media-impact-on-mental-health-in-india/avg_time_spent_worldwide.csv")
age_data_long <- read.csv("../input/social-media-impact-on-mental-health-in-india/age_data_long.csv")

global_avg <- df_sorted %>% filter(region == "Global Average") %>% pull(users)



### 2.1 User Count Worldwide

ggplot(df_sorted %>% mutate(highlight = ifelse(region == "Global Average", "Global Average", "")), 
       aes(x = fct_reorder(region, users), y = users, fill = highlight)) + 
  geom_bar(stat = "identity") +
  scale_fill_manual(values = c("gray80", "red")) + # Highlight global average row in red
  geom_hline(yintercept = global_avg, color = "red", linetype = "dashed", 
             size = 1) + # Add horizontal line for global average
  geom_text(aes(label = users_percent), 
            position = position_stack(vjust = 0.5), # Stack labels on top of bars
            size = 3, 
            color = "white") + # Add percentage labels
  coord_flip() +
  labs(title = "Social Media Users vs. Total Population - Oct 2022",
       subtitle = "Active Social Media Users As A Percentage of The Total Population", 
       x = "", y = "Percent Users",
       caption = "Data Source: DataReportal\nHootsuite") +
  theme_minimal() +
  guides(fill=FALSE) + # Remove legend
  theme(plot.title = element_text(size = 18, hjust = 0.5),
        plot.subtitle = element_text(size = 12, hjust = 0.5),
        plot.margin = unit(c(1, 2, 1, 1), "cm")) # Adjust plot margin to make it wider


### 2.2 Countries by Internet Users


df4_country <- df4 %>% 
  arrange(desc(users))

df4_country %>%
  ggplot(aes(x = fct_reorder(country, users), y = users)) +
  geom_col(fill = "#0072B2") +
  geom_text(aes(label = scales::comma(users), hjust = -0.2), color = "darkblue", size = 3.5) +
  scale_y_continuous(limits = c(0, 1200), expand = c(0, 0), breaks = seq(0, 1200, 200)) +
  labs(title = "Countries By Internet Users", subtitle = "Oct 2022",
       x = "Country",
       y = "Number of Internet Users (Millions)",
       caption = "Data Source: Statista") +
  theme_minimal() +
  theme(plot.title = element_text(size = 18, face = "bold", color = "darkgray"),
        plot.subtitle = element_text(size = 12, face = "bold", color = "darkgrey"),
        axis.title = element_text(size = 14, color = "darkgray"),
        axis.text.x = element_text(size = 12, hjust = 1),
        axis.text.y = element_text(size = 12, color = "darkgray"),
        plot.caption = element_text(hjust = 0, color = "darkgray"),
        panel.grid.major.y = element_line(color = "lightgray")) +
  coord_flip()

### 2.3 Average Usage Worldwide

library(ggplot2)

avg_time_spent_worldwide %>%
  ggplot(aes(x = as.numeric(year), y = time)) +
  geom_line(color = "#0072B2", size = 1.5) +
  geom_point(color = "#0072B2", size = 3) +
  geom_text(aes(label = time), vjust = -1.5, color = "#0072B2") +
  scale_x_continuous(breaks = seq(2012, 2022, 1), limits = c(2012, 2022)) +
  scale_y_continuous(breaks = seq(0, 150, 10), limits = c(0, 150)) +
  labs(title = "Average Daily Time Spent On Social Media Worldwide",
       x = "Year",
       y = "Minutes",
       caption = "Data Source: Statista") +
  theme_minimal() +
  theme(plot.title = element_text(size = 16, face = "bold", color = "darkgray"),
        axis.title = element_text(size = 14),
        axis.text = element_text(size = 12, color = "darkgray"),
        plot.caption = element_text(hjust = 0, color = "darkgray"),
        axis.title.x = element_text(size = 14, color = "darkgray"),
        axis.title.y = element_text(size = 14, color = "darkgray"),
        panel.grid.major = element_line(color = "lightgray"),
        panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        panel.background = element_blank(),
        legend.position = "none")



### 2.4 Users by Age

# reshape data into long format
#age_data_long <- df3 %>% 
 # pivot_longer(cols = c(`2013-2019`, `2019-2025`), names_to = "year_range", values_to = "value") %>%
  #mutate(year_range = str_replace(year_range, "-", " - "))


# create bar chart
age_plot <- ggplot(age_data_long, aes(x = age, y = value, fill = year_range)) +
  geom_bar(stat = "identity", position = "dodge", color = "black") +
  scale_fill_manual(values = c("steelblue", "darkblue"), name = " ", 
                    labels = c("2013 - 2019", "2019 - 2025")) +
  labs(title = "Internet Usage by Age Group In India", x = NULL, y = "Percentage", 
       caption = "Data Source: Statista") +
  theme_minimal() +
  theme(plot.title = element_text(size = 18, face = "bold", color = "darkslategrey"),
        axis.text = element_text(size = 12, color = "darkslategrey"),
        axis.title = element_text(size = 14, color = "darkslategrey"),
        legend.position = "bottom",
        panel.grid.major = element_line(color = "lightgrey"),
        panel.grid.minor = element_blank())

# add data labels to bars
age_plot +
  geom_text(aes(label = paste0(value, "%")), 
            position = position_dodge(width = 1), 
            vjust = -0.5, color = "black")

# reshape data into long format
df8 <- df5 %>% 
  pivot_longer(cols = c("men", "women"), names_to = "gender", values_to = "percentage")


class(df8$percentage)
df8$percentage <- as.numeric(gsub("%", "", df8$percentage))
colors <- c("#0072B2", "lightblue","darkblue")

### 2.5 Disorders by Gender

ggplot(df8, aes(x = "", y = percentage, fill = disorders)) +
  geom_bar(stat = "identity", width = 1, color = "white") +
  coord_polar(theta = "y") +
  facet_wrap(~ gender) +
  scale_fill_manual(values = colors, labels = c("Stress", "Depression", "Anxiety")) +
  theme_void() +
  theme(legend.position = "bottom",
        plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
        plot.subtitle = element_text(size = 12, hjust = 0.5),
        legend.title.align = 0.5,
        legend.text = element_text(size = 11),
        axis.text = element_blank(),
        axis.ticks = element_blank(),
        plot.caption = element_text(size = 11, color = "darkgrey", vjust = 0.5)) +
  geom_text(aes(label = paste0(percentage, "%")), position = position_stack(vjust = 0.5), size = 4, color = "white") +
  scale_y_continuous(limits = c(0, 100), expand = c(0, 0)) +
  labs(title = "Indian Mental Health Disorders by Gender",
       subtitle = "2021",
       fill = " ",
       caption = "Source: Digital Mental Health Innovations in India Report 2021, page 5")
```

### 2.6 Impact on Youth


ggplot(df_long, aes(x = stringr::str_wrap(statement, width = 30), y = value, fill = variable)) +
  geom_bar(stat = "identity") +
  scale_fill_viridis_d(option = "D") +
  coord_flip() +
  labs(title = "Impact of Instagram on Young Adults",
       subtitle = "Survey 2020",
       x = "", y = "Percentage of Responses", fill = "",
       caption = "Data Source: The Impact of Instagram on Young Adults Social Comparison, 
Colourism and Mental Health: Indian Perspective\nInternational Journal of Information Management Data Insights\nVolume 2, 
Issue 1, April 2022\nSurvey data collected between 23 September 2020 to 05 October 2020") +
  theme_minimal() +
  theme(legend.position = "bottom",
        axis.text.x = element_text(angle = 0, hjust = 1,
                                   vjust = 0.5,
                                   margin = margin(t = 0, r = 0, b = 30, l = 0)),
        plot.caption = element_text(size = 8)) +
  geom_text(aes(label = paste0(sprintf("%.2f", value*1),"%")),
            position = position_stack(vjust = 0.5), size = 3, color = "white")

### 2.7 Effective Actions

df_long_response <- melt(df7, id.vars = "actions")

# Add percentage labels to the bars
df_long_response <- df_long_response %>%
  group_by(actions, variable) %>%
  mutate(percent = paste0(value, "%"))

# Create a stacked bar chart with viridis color palette
ggplot(df_long_response, aes(x = actions, y = value, fill = variable)) +
  geom_col(position = "stack", color = "white", width = 0.8) +
  scale_fill_viridis_d(option = "E") +
  coord_flip() +
  geom_text(aes(label = percent), position = position_stack(vjust = 0.5), size = 4, color = "white") +
  labs(title = "Effectiveness of Mental Health Actions - 2020",
       subtitle = "Percentage of respondents who found the actions helpful or not helpful",
       y = "Percentage",
       x = " ",
       fill = "",
       caption = "Source: Wellcome Global Monitor 2020: The role of science in mental health, page 29") +
  theme(plot.title = element_text(size = 16, face = "bold"),
        plot.subtitle = element_text(size = 12),
        axis.title = element_text(size = 12),
        axis.text = element_text(size = 10),
        legend.title = element_blank(),
        legend.text = element_text(size = 10),
        legend.position = "bottom",
        plot.caption = element_text(size = 10, color = "slategray")) +
  scale_y_continuous(expand = c(0, 0), limits = c(0, 100))
