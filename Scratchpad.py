# Databricks notebook source
# MAGIC %run ./02-setup

# COMMAND ----------

SH = SetupHelper("dev")
SH.cleanup()


# COMMAND ----------

SH.setup()

# COMMAND ----------

SH.validate()


# COMMAND ----------

# MAGIC %run ./03-history-loader

# COMMAND ----------

H = HistoryLoader("dev")
H.load_history()

# COMMAND ----------

H.validate()
