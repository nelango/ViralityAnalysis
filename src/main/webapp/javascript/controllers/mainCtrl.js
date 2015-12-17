
myApp = angular.module('myApp.controllers', ['nvd3'])
.controller('mainCtrl',['$scope','$rootScope', '$http', function ($scope,$rootScope,$http) {

    console.log("Response in the result page:"+$rootScope.response);
    var response = $rootScope.response;
    $scope.response = response;
    var formData = $rootScope.formData;


if (typeof(current) !== 'undefined'){
        window.nv.charts = {};
        window.nv.graphs = [];
        window.nv.logs = {};
        // remove resize listeners
        window.onresize = null;
    }
            $scope.options = {

                chart: {
                type: 'multiBarHorizontalChart',
                height: 900,
                x: function(d){return d.label;},
                y: function(d){return d.value;},
                showControls: true,
                showValues: true,
                showXAxis: false,
                duration: 500,
                xAxis: {
                    showMaxMin: false
                },
                yAxis: {
                    axisLabel: 'Values',
                    tickFormat: function(d){
                        return d3.format(',.2f')(d);
                    }
                }
            }
        };

        $scope.data = [
            {
                "key": "Share Buckets",
                "color": "#d62728",
                "values": [
                    {
                        "label" : "Less than 100" ,
                        "value" : response.sharesLessThanHundred
                    } ,
                    {
                        "label" : "100 to 1000" ,
                        "value" : response.sharesHundredToThousand
                    } ,
                    {
                        "label" : "1000 to 10,000" ,
                        "value" : response.sharesThousandToTenThousand
                    } ,
                    {
                        "label" : "Greater than 10,000" ,
                        "value" : response.sharesGreaterThanTenThousand
                    }
                    
                ]
            },
            {
                "key": "Sentiment Analysis",
               // "color": "#1f77b4",
                "values": [
                    {
                        "color": "#1f77b4",
                        "label" : "Polarity of Title (User)" ,
                        "value" : response.titlePolarity
                    } ,


                    {
                        "color": "#00FF00",
                        "label" : "Polarity of Title (Dataset)" ,
                        "value" : response.avgTitleSentimentPolarity
                    } ,


                    {
                        "color": "#1f77b4",
                        "label" : "Subjectivity of Title (User)" ,
                        "value" : response.titleSubjectivity
                    } ,

                    {
                        "color": "#00FF00",
                        "label" : "Subjectivity of Title (Dataset)" ,
                        "value" : response.avgTitleSubjectivity
                    } ,
                    
                   
                    {
                        "color": "#1f77b4",
                        "label" : "Negative Rate of Content (User)" ,
                        "value" : response.contentNegativeRate
                    } ,


                    {
                        "color": "#00FF00",
                        "label" : "Negative Rate of Content (Dataset)" ,
                        "value" : response.avgRateNegativeWords
                    } ,

                    {
                        "color": "#1f77b4",
                        "label" : "Positive Rate of Content (User)" ,
                        "value" : response.contentPositiveRate
                    } ,

                    {
                        "color": "#00FF00",
                        "label" : "Positive Rate of Content (Dataset)" ,
                        "value" : response.avgRatePositiveWords
                    } ,

                    {
                        "color": "#1f77b4",
                        "label" : "Polarity of Content (User)" ,
                        "value" : response.contentSentimentPolarity
                    } ,

                    {
                        "color": "#1f77b4",
                        "label" : "Subjectivity of Content (User)" ,
                        "value" : response.contentSubjectivity
                    } ,

                    {
                        "color": "#00FF00",
                        "label" : "Subjectivity of Content (Dataset)" ,
                        "value" : response.avgGlobalSubjectivity
                    } 

                    ]
                },

                {
                "key": "User Input v/s Dataset",
               // "color": "#00FF00",
                "values": [
                    {
                        "color": "#00FF00",
                        "label" : "Average #Images (Dataset)" ,
                        "value" : response.avgImagesNumber
                    } ,

                    {
                        "color": "#1f77b4",
                        "label" : "Number of Images (User)" ,
                        "value" : formData.imagesNumber
                    } ,

                    {
                        "color": "#00FF00",
                        "label" : "Average #Videos (Dataset)" ,
                        "value" : response.avgVideosNumber
                    } ,

                    {
                        "color": "#1f77b4",
                        "label" : "Number of Videos (User)" ,
                        "value" : formData.videosNumber
                    } ,

                    {
                        "color": "#00FF00",
                        "label" : "Average #Keywords (Dataset)" ,
                        "value" : response.avgKeywords
                    },

                    {
                        "color": "#1f77b4",
                        "label" : "Number of Keywords (User)" ,
                        "value" : formData.keywords
                    },

                    {
                        "color": "#00FF00",
                        "label" : "Average #Links (Dataset)" ,
                        "value" : response.avgLinksNumber
                    },

                    {
                        "color": "#1f77b4",
                        "label" : "Number of Links (User)" ,
                        "value" : formData.linksNumber
                    }
                    
                ]
            },

            {
                "key": "Day Analysis",
                "color": "#FDB45C",
                "values": [
                    {
                        "label" : "Shares on Sunday" ,
                        "value" : response.daySunday
                    } ,
                    {
                        "label" : "Shares on Monday" ,
                        "value" : response.dayMonday
                    } ,

                    {
                        "label" : "Shares on Tuesday" ,
                        "value" : response.dayTuesday
                    },

                    {
                        "label" : "Shares on Wednesday" ,
                        "value" : response.dayWednesday
                    },
                    {
                        "label" : "Shares on Thursday" ,
                        "value" : response.dayThursday
                    },
                    
                    {
                        "label" : "Shares on Friday" ,
                        "value" : response.dayFriday
                    },

                    {
                        "label" : "Shares on Saturday" ,
                        "value" : response.daySaturday
                    }
                ]
            },


            {
                "key": "Category Analysis",
                "color": "#DCDCDC",
                "values": [
                    {
                        "label" : "Social Media" ,
                        "value" : response.categorySocMed
                    } ,
                    {
                        "label" : "Business" ,
                        "value" : response.categoryBus
                    } ,

                    {
                        "label" : "World" ,
                        "value" : response.categoryWorld
                    },

                    {
                        "label" : "Technology" ,
                        "value" : response.categoryTech
                    },
                    {
                        "label" : "Entertainment" ,
                        "value" : response.categoryEntertainment
                    },
                    
                    {
                        "label" : "Lifestyle" ,
                        "value" : response.categoryLifestyle
                    }
                ]
            }
            
            ]}]);