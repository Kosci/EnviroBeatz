var app = angular.module('enviroBeatzApp', []);
app.controller('songController', function($scope, $http) {
    $scope.song = null;
    $scope.songUrl = null;
    $scope.songName = null;

    $scope.songType = null;

    $scope.songId = null;

    $scope.songTemp = null;
    $scope.temp_min = 0;
    $scope.temp_max = 0;
    
    $scope.songLight = null;
    $scope.light_min = 0;
    $scope.light_max = 0;

    console.log("Loves");

    $scope.submit = function () {
        //If song is light
        if ($scope.songType == 0)
        {
            $scope.songLight.songId = $scope.songId;
            $scope.songLight.light_min = $scope.light_min;
            $scope.songLight.light_max = $scope.light_max;
            
            console.log($scope.songLight);
            //$http.post('/envirobeatz/api/v1.0/songs/addSongLight' , songLight);
        }

        else if ($scope.songType = 1)
        {
            $scope.songTemp.songId = $scope.songId;
            $scope.songTemp.temp_min = $scope.light_min;
            $scope.songTemp.temp_max = $scope.light_max;

            console.log($scope.songTemp);
            //$http.post('/envirobeatz/api/v1.0/songs/addSongTemp' , songTemp);
        }
    };

    $scope.onTypeChange = function ()
    {
        console.log()
        if ($("#valueContainer").length > 0)
        {
            $("#hiddenContainer").append($("#lightOptions"));
            $("#hiddenContainer").append($("#tempOptions"));
        }
        if ($scope.songType == 0)
        {
            $("#valueContainer").append($("#lightOptions"));
        }
        else
        {
            $("#valueContainer").append($("#tempOptions"));
        }
    }
});