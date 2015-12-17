'use strict';

angular.module('myApp', [
    'myApp.controllers',
    'ngRoute'
    ])

.config(function ($routeProvider,$httpProvider){

  $routeProvider.when('/home', {templateUrl: 'views/home.html', controller: 'HomeController'});
  $routeProvider.when('/result', {templateUrl: 'views/result.html', controller: 'mainCtrl'});
  $routeProvider.otherwise({redirectTo: '/home'});

  /* CORS... */
  $httpProvider.defaults.headers.common['Access-Control-Allow-Origin']='*';
  $httpProvider.defaults.useXDomain = true;
  delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

