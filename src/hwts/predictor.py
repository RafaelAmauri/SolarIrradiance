import os
import pandas             as pd
import matplotlib.pyplot  as plt
import numpy              as np

from datetime                     import datetime
from dateutil.relativedelta       import relativedelta
from statsmodels.tsa.holtwinters  import ExponentialSmoothing


class Predictor:
    ## Year where the time series starts 
    __tseries_start: datetime

    ## Year where the time series ends
    __tseries_end: datetime

    ## A float indicating the smoothing of the level of the time series.
    ## When values for this variable increase, the model gives increasing 
    ## relevance to more recent entries, to the detriment of the relevance 
    ## of older entries.
    ## Default = 0.1
    __tseries_smoothing_level: float

    ## A float indicating the smoothing of the seasonality of the time series.
    ## When values for this variable increase, the model gives increasing 
    ## relevance to more recent entries, to the detriment of the relevance 
    ## of older entries.
    ## Default = 0.2
    __tseries_smoothing_seasonal: float

    ## Lists containing training and testing values, as well
    ## as the dates refering to each of them
    __training_dataset: list
    __training_dates: list
    __testing_dataset: list
    __testing_dates: list

    ## Predictions made by the model
    __predictions: list

    ## How many years will be used for training. Can't be lower than 2
    ## because the ML model needs at least 2 years to take note of seasonality.
    ## Default = 2
    __num_training_years: int

    ## Exports the predictions and observed values for each year to a png. 
    ## Default = True
    __save_chart_for_each_year: bool

    ## Exports the predictions and observed values for the whole testing period to a single png. 
    ## Default = True
    __save_chart_single: bool

    ## Exports a chart with the absolute errors for each prediction relative to its observed value to a png. 
    ## Default = True
    __save_chart_absolute_errors:bool

    ## Lower and upper limits for y in charts.
    ## Default upper limit = 8 // Default lower limit = 3
    __chart_y_upper_limit: float
    __chart_y_lower_limit: float

    ## Folder where the charts will be exported to.
    ## Default = "./predictions"
    __charts_export_location: str

    ## Height of the chart.
    ## Default = 25.6
    __chart_height = float

    ## Width of the chart.
    ## Default = 14.4
    __chart_width: float

    ## Chart's font size.
    ## Default = 18
    __chart_fontsize: float

    ## Size of the legend of the chart.
    ## Default = 27
    __chart_legendsize: float

    ## Width of the lines in the chart.
    ## Default = 4
    __chart_linewidth: float

    def __init__(self):

        ## Default values :)
        ## These be changed at will by using the setters
        self.save_chart_for_each_year = True
        self.save_chart_single = True
        self.save_chart_absolute_errors = True
        self.chart_y_upper_limit = 8
        self.chart_y_lower_limit = 3
        self.chart_height = 25.6
        self.chart_width = 14.4
        self.chart_fontsize = 18
        self.chart_legendsize = 27
        self.chart_linewidth = 4
        self.num_training_years = 2
        self.tseries_smoothing_level = 0.1
        self.tseries_smoothing_seasonal = 0.2


    ## Getters and Setters
    @property
    def tseries_start(self) -> int:
        return self.__tseries_start

    @tseries_start.setter
    def tseries_start(self, start_year: int):
        self.__tseries_start = datetime(start_year, 1, 1)

    @property
    def tseries_end(self) -> int:
        return self.__tseries_end
    
    @tseries_end.setter
    def tseries_end(self, end_year: int):
        self.__tseries_end = datetime(end_year, 12, 31)

    @property 
    def predictions(self) -> list:
        return self.__predictions
    
    @predictions.setter
    def predictions(self, pred: list):
        self.__predictions = pred

    @property
    def tseries_smoothing_level(self) -> float:
        return self.__tseries_smoothing_level
    
    @tseries_smoothing_level.setter
    def tseries_smoothing_level(self, smoothing: float):
        self.__tseries_smoothing_level = smoothing

    @property 
    def tseries_smoothing_seasonal(self) -> float:
        return self.__tseries_smoothing_seasonal
    
    @tseries_smoothing_seasonal.setter
    def tseries_smoothing_seasonal(self, smoothing: float):
        self.__tseries_smoothing_seasonal = smoothing

    @property
    def num_training_years(self) -> int:
        return self.__num_training_years
    
    @num_training_years.setter
    def num_training_years(self, num_years: int):
        self.__num_training_years = num_years

    @property
    def save_chart_for_each_year(self) -> bool:
        return self.__save_chart_for_each_year
    
    @save_chart_for_each_year.setter
    def save_chart_for_each_year(self, export_charts: bool):
        self.__save_chart_for_each_year = export_charts

    @property
    def save_chart_single(self) -> bool:
        return self.__save_chart_single
    
    @save_chart_single.setter
    def save_chart_single(self, export_charts: bool):
        self.__save_chart_single = export_charts

    @property
    def save_chart_absolute_errors(self) -> bool:
        return self.__save_chart_absolute_errors
    
    @save_chart_absolute_errors.setter
    def save_chart_absolute_errors(self, export_charts: bool):
        self.__save_chart_absolute_errors = export_charts

    @property
    def chart_y_upper_limit(self) -> float:
        return self.__chart_y_upper_limit

    @chart_y_upper_limit.setter
    def chart_y_upper_limit(self, limit: float):
        self.__chart_y_upper_limit = limit

    @property
    def chart_y_lower_limit(self) -> float:
        return self.__chart_y_lower_limit

    @chart_y_lower_limit.setter
    def chart_y_lower_limit(self, limit: float):
        self.__chart_y_lower_limit = limit
    
    @property
    def charts_export_location(self) -> str:
        return self.__charts_export_location
    
    @charts_export_location.setter
    def charts_export_location(self, location: str):
        if not os.path.exists(location):
            os.makedirs(location)

        self.__charts_export_location = location

    @property
    def chart_height(self) -> float:
        return self.__chart_height

    @chart_height.setter
    def chart_height(self, height: float):
        self.__chart_height = height

    @property
    def chart_width(self) -> float:
        return self.__chart_width

    @chart_width.setter
    def chart_width(self, width: float):
        self.__chart_width = width

    @property
    def chart_fontsize(self) -> float:
        return self.__chart_fontsize

    @chart_fontsize.setter
    def chart_fontsize(self, fontsize: float):
        self.__chart_fontsize = fontsize

    @property
    def chart_legendsize(self) -> float:
        return self.__chart_legendsize

    @chart_legendsize.setter
    def chart_legendsize(self, legendsize: float):
        self.__chart_legendsize = legendsize

    @property
    def chart_linewidth(self) -> float:
        return self.__chart_linewidth

    @chart_linewidth.setter
    def chart_linewidth(self, linewidth: float):
        self.__chart_linewidth = linewidth

    ## Given a list of IDs, forecast values of solar irradiance for each entry.
    ## Ideally you just need to call this one function and let it orchestrate
    ## other function calls.
    ## @params:
    ##  stations -> list of IDs of the stations to be forecasted
    ##  datasets_location -> String with the path for the folder that holds 
    ##      the data for the stations
    def plot_predictions(self, stations: list, datasets_location: str):
        if not isinstance(self.tseries_start, datetime) or not isinstance(self.tseries_end, datetime):
            raise Exception("Make sure to set the start and end of the time series!")

        if self.tseries_end < self.tseries_start:
            raise Exception("Time series cannot have an end date lower than the start date!")

        if not hasattr(self, "charts_export_location"):
            raise Exception("Please select a folder to export your charts to first!")
    
        ## How many years the time series lasts. This is important to iterate
        ## over the series with different training sizes. The + 1 is to make it inclusive
        ## of the last year.
        duration_tseries_years = self.tseries_end.year - self.tseries_start.year + 1

        for station_id in stations:
            if not os.path.exists(f"{self.charts_export_location}{os.sep}{station_id}"):
                os.makedirs(f"{self.charts_export_location}{os.sep}{station_id}")

            self._split_train_test(self.num_training_years, station_id, datasets_location)

            self.predictions = []

            ## Auxiliar array for adding more data to training without 
            ## affecting self.__training_dataset
            testing_aux = self.__testing_dataset.copy()

            for year in range(self.num_training_years, duration_tseries_years):
                self.predictions.extend(ExponentialSmoothing(
                                            initialization_method = 'estimated',
                                            endog = np.asarray(self.__training_dataset),
                                            trend = None,
                                            seasonal = 'add',
                                            seasonal_periods = 12
                                        ).fit(
                                            smoothing_level = self.tseries_smoothing_level,
                                            smoothing_seasonal = self.tseries_smoothing_seasonal
                                        ).forecast(
                                            steps = 12
                                        )
                                    )
        
                ## Since the goal of the paper is to predict only the next
                ## 12 months, here we move the next year (12 months) from the testing
                ## database to the training database
                self.__training_dataset.extend(testing_aux[0 : 12])

                ## Deleting the first 12 elements so we can simply 
                ## extend self.__training_dataset by the first 12 elements
                ## every time
                del testing_aux[0 : 12]

            if self.save_chart_single:
                self._export_chart_single(station_id)
                
            if self.save_chart_absolute_errors:
                self._export_chart_absolute_errors(station_id)
                
            if self.save_chart_for_each_year:
                self._export_chart_for_each_year(station_id, duration_tseries_years)


    ## Splits the data into training and testing datasets. Also finds the dates for the X axis
    ## on the charts.
    ## @params: 
    ##      num_training_years  -> How many years will be used for training
    ##      station_id          -> The ID of the station
    ##      datasets_location   -> The location of the folder that holds the CSVs
    def _split_train_test(self, num_training_years, station_id, datasets_location):

        # Hacky way to figure out the training period for the series
        d1 = self.tseries_start
        d2 = self.tseries_start + relativedelta(years=num_training_years) - relativedelta(days=1)

        self.__training_dates   = []
        self.__training_dataset = []
        self.__testing_dates    = []
        self.__testing_dataset  = []

        while d1 <= d2:
            self.__training_dates.append(datetime.strftime(d1, '%-m/%-y'))
            d1 += relativedelta(months=1)

        d2 += relativedelta(days=1)

        while d2 <= self.tseries_end:
            self.__testing_dates.append(datetime.strftime(d2, '%-m/%-y'))
            d2 += relativedelta(months=1)

        # Obtaining dataset file
        df = pd.read_csv(f"{datasets_location}{os.sep}{station_id}.csv", sep=";")
        
        # Obtaining training dataset
        for entry in df[station_id][0 : len(self.__training_dates)]:
            self.__training_dataset.append(entry)

        # Obtaining testing dataset
        for entry in df[station_id][len(self.__training_dates) : len(self.__training_dates) + len(self.__testing_dates)]:
            self.__testing_dataset.append(entry)


    ## Exports a chart containing the observed and predicted irradiance values
    ## to a single chart.
    ## @params: 
    ##      station_id -> ID of the station
    def _export_chart_single(self, station_id: str):

        ## Setting up configurations for the chart
        figure = plt.figure(figsize=(self.chart_height, self.chart_width))
        axis = figure.gca()

        axis.set_ylim([self.chart_y_lower_limit, self.chart_y_upper_limit])
        axis.set_ylabel("kWh/m²/day", labelpad=80, rotation='horizontal', fontsize=self.chart_legendsize)

        ## There are so many dates in the dataset, this is the only way to make the legend readable! AVOID CHANGING!!
        axis.set_xticks([x for x in list(range(0, len(self.__testing_dates))) if x % 3 == 0])

        axis.tick_params(axis='x', labelrotation=45, labelsize=self.chart_fontsize)
        axis.tick_params(axis='y', labelsize=self.chart_fontsize)

        axis.plot(self.__testing_dates, self.__testing_dataset, linewidth=self.chart_linewidth)
        axis.plot(self.__testing_dates, self.predictions, linewidth=self.chart_linewidth)

        axis.legend(['Observed Values', 'Predicted Values'], fontsize=self.chart_fontsize)

        ## Saving chart
        figure.savefig(f"{self.charts_export_location}{os.sep}{station_id}{os.sep}{station_id}.png")

        ## Cleaning chart
        plt.close(figure)


    ## Exports a chart containing the absolute value of the deviation
    ## between observed and predicted values to a single chart.
    ## @params: 
    ##      station_id -> ID of the station
    def _export_chart_absolute_errors(self, station_id: str):
        
        ## To calculate the erros, first we need to find by how much our model missed the actual
        ## observed value. This is stored in <deviations>
        deviations = []
        for x, y in zip(self.predictions, self.__testing_dataset):
            deviations.append(x - y)

        figure = plt.figure(figsize=(self.chart_height, self.chart_width))
        axis = figure.gca()
        
        axis.set_ylim([-3, 3])
        axis.set_ylabel("kWh/m²/day", labelpad=80, rotation='horizontal', fontsize=self.chart_legendsize)
        axis.set_xticks([x for x in list(range(0, len(self.__testing_dates))) if x % 3 == 0])

        axis.tick_params(axis='x', labelrotation=45, labelsize=self.chart_fontsize)
        axis.tick_params(axis='y', labelsize=self.chart_fontsize)

        axis.plot(self.__testing_dates, deviations, linewidth=self.chart_linewidth)

        axis.legend(["Absolute Error"], fontsize=self.chart_fontsize)

        ## Calculating MAE Score
        deviations_absolute = [abs(x) for x in deviations]
        mae_score = np.mean(deviations_absolute)

        print(f"MAE Score = {mae_score:.2f}")

        ## Saving chart
        figure.savefig(f"{self.charts_export_location}{os.sep}{station_id}{os.sep}{station_id}_deviation.png")

        plt.close(figure)


    ## Exports a chart containing the observed and predicted irradiance values
    ## for each of the years in the time series to a separate image. Ideally used
    ## to help with visualization.
    ## @params: 
    ##      station_id -> ID of the station
    ##      duration_tseries_years: number of years in the time series
    def _export_chart_for_each_year(self, station_id: str, duration_tseries_years: int):
        for year in range(duration_tseries_years - self.num_training_years):
            ## For each year, find what are the dates for that year, predicted 
            ## values and also the observed values.
            dates_current_year = self.__testing_dates[12*year : 12*(year+1)]
            predictions_current_year = self.predictions[12*year : 12*(year+1)]
            observed_values_current_year = self.__testing_dataset[12*year : 12*(year+1)]

            figure = plt.figure(figsize=(self.chart_height, self.chart_width))
            axis = figure.gca()

            axis.set_ylim([self.chart_y_lower_limit, self.chart_y_upper_limit])
            axis.set_ylabel("kWh/m²/day", labelpad=80, rotation='horizontal', fontsize=self.chart_legendsize)

            axis.tick_params(axis='x', labelsize=self.chart_fontsize)
            axis.tick_params(axis='y', labelsize=self.chart_fontsize)

            axis.plot(dates_current_year, observed_values_current_year, linewidth=self.chart_linewidth)
            axis.plot(dates_current_year, predictions_current_year, linewidth=self.chart_linewidth)

            axis.legend(['Observed Values', 'Predicted Values'], fontsize=self.chart_fontsize)

            figure.savefig(f"{self.charts_export_location}{os.sep}{station_id}{os.sep}{station_id}_{self.tseries_start.year + self.num_training_years + year}.png")
            
            plt.close(figure)