var app = angular.module('enviroBeatzApp', []);
app.controller('songController', function($scope, $http) {
    $scope.song = null;
    $scope.url = null;

    //Pass this in
    $scope.type = "light";

    //$scope.songId = null;

    $scope.min = 0;
    $scope.max = 0;
    
    $scope.submit = function () {
        
        console.log($scope.song);
        $http.post('/envirobeatz/api/v1.0/songs/add' , $scope.song);
    };

});