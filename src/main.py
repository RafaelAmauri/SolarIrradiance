import hwts.predictor

pred = hwts.predictor.Predictor()

pred.tseries_start = 2015
pred.tseries_end = 2020
pred.num_training_years = 2
pred.charts_export_location = "./predictions"

pred.plot_predictions(["A555", "A510", "A513", "A521", "A552", "A556", "A557", "A729"], "./stations")