library(dplyr)
library(ggplot2)

conn <- DBI::dbConnect(RSQLite::SQLite(), "cpu_temp_monitor.db")

df <-
  DBI::dbGetQuery(conn, "SELECT * FROM cpu_temp") %>% 
  mutate(datetime = lubridate::as_datetime(datetime)) %>% 
  filter(as.Date(datetime) <= Sys.Date() - 1,
         as.Date(datetime) >= Sys.Date() - 7)

DBI::dbDisconnect(conn)

g <- 
  ggplot(data = df,
       aes(x = datetime,
           y = temp)) +
  geom_point() +
  geom_smooth(se = FALSE) +
  scale_x_datetime(date_labels = "%e %b",
                   date_breaks = "1 days",
                   date_minor_breaks = "1 days") +
  labs(title = "CPU temperature",
       subtitle = paste0(Sys.Date() - 7, " -- ", Sys.Date() - 1),
       x = element_blank(),
       y = "Temperature (C)") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5),
        plot.subtitle = element_text(hjust = 0.5))


options(bitmapType = "cairo")
ggsave("eloelo.png", g, device = "png")
