
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator

class ModelMetrics():

    #@classmethod
    def get_metrics_predictions(self, df_with_labels_and_predictions, args):
        metrics = ["accuracy", "weightedPrecision", "weightedRecall", "f1", "areaUnderROC", "areaUnderPR"]
        val_metrics = {}
        for metric in metrics:
            val_metrics[metric] = self.get_metric(df_with_labels_and_predictions, metric)
        return val_metrics["accuracy"], val_metrics["areaUnderROC"], val_metrics["weightedPrecision"], \
               val_metrics["weightedRecall"], val_metrics["f1"], val_metrics["areaUnderPR"]

    def get_metric(self, df_predictions, metric = "accuracy"):
        if metric in ["accuracy", "weightedPrecision", "weightedRecall", "f1"]:
            evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName=metric)
            value = evaluator.evaluate(df_predictions)
        elif metric in ["areaUnderROC", "areaUnderPR"]:
            evaluator = BinaryClassificationEvaluator(labelCol="label", rawPredictionCol="prediction", metricName=metric)
            value = evaluator.evaluate(df_predictions)
        else:
            print("Do not exist Metric Name --> {}".format(metric))
        return value