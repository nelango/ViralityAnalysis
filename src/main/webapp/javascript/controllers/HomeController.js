'use strict';

/* Controller */

var myApp = angular.module('myApp.controllers')
.controller('HomeController', ['$scope','$http','$rootScope','$location','$window',function ($scope,$http,$rootScope,$location,$window) {


    console.log("Hello");
    $scope.share={};
    $rootScope.response={};
    $scope.formData = {};

    $scope.days = [
     { name: 'Monday' },
     { name: 'Tuesday' },
     { name: 'Wednesday' },
     { name: 'Thursday' },
     { name: 'Friday' },
     { name: 'Saturday' },
     { name: 'Sunday' },
   ];    

    $scope.categories = [
     { name: 'Lifestyle' },
     { name: 'Entertainment' },
     { name: 'Business' },
     { name: 'Social Media' },
     { name: 'Tech' },
     { name: 'World' },
   ];   

    $scope.submit = function() {

        $http.post("http://localhost:8080/api/article/predict", $scope.formData).
        success(
            function(response) {
                $rootScope.formData = $scope.formData;
                console.log(response);
                $rootScope.response=response;
                //$location.path('http://localhost:8080/#/result');
                $location.url("/result");
                $window.location.href="http://localhost:8080/#/result";
                console.log("Hello again");

            })
        .error(function(){
            console.log("Error");
        });
    }
}]);