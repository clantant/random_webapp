// For an introduction to the Blank template, see the following documentation:
// http://go.microsoft.com/fwlink/?LinkId=232509
(function () {
	"use strict";

	var app = WinJS.Application;
	var activation = Windows.ApplicationModel.Activation;

	app.onactivated = function (args) {
		if (args.detail.kind === activation.ActivationKind.launch) {
			if (args.detail.previousExecutionState !== activation.ApplicationExecutionState.terminated) {
				// TODO: This application has been newly launched. Initialize your application here.
			} else {
				// TODO: This application was suspended and then terminated.
				// To create a smooth user experience, restore application state here so that it looks like the app never stopped running.
			}

			var geolocator = new Windows.Devices.Geolocation.Geolocator();

			var nav = new WinJS.UI.SplitView();

			args.setPromise(WinJS.UI.processAll().then(function completed() {
			    var ratingControlDiv = document.getElementById("ratingControlDiv");
                
			    var ratingControl = ratingControlDiv.winControl;
                
			    ratingControl.addEventListener("change", ratingChange, false);

			    // Retrieve the button and register our event handler.
			    var helloButton = document.getElementById("helloButton");
			    helloButton.addEventListener("click", buttonClickHandler, false);
			}));

		}
	};

	app.oncheckpoint = function (args) {
		// TODO: This application is about to be suspended. Save any state that needs to persist across suspensions here.
		// You might use the WinJS.Application.sessionState object, which is automatically saved and restored across suspension.
		// If you need to complete an asynchronous operation before your application is suspended, call args.setPromise().
	};

	function pos(eventInfo) {
        var coord = pos.coordinate;

	    var settings = Windows.Storage.ApplicationData.current.localSettings;
	    settings.values["Status"] = coord.timestamp;

	    settings.values["latitude"] = coord.point.position.latitute;
	    settings.values["longitute"] = coord.point.position.longitute;
	    settings.values["accuracy"] = coord.accuracy;

	    backgroundTaskInstance.succeeded = true;

	    close();
	}
	function err(eventInfo) {
	    var settings = Windows.Storage.ApplicationData.current.localSettings;

	    settings.values["Status"] = err.message;

	    settings.values["latitude"] = "No data";
	    settings.values["longitude"] = "No data";
	    settings.values["accuracy"] = "No data";

	    backgroundTaskInstance.succeeded = false;

	    close();
	}



	function buttonClickHandler(eventInfo) {
	    var userName = document.getElementById("nameInput").value;
	    var greetingString = "Hello, " + userName + "!";
	    document.getElementById("greetingOutput").innerText = greetingString;
	}

	function ratingChange(eventInfo) {
	    var ratingOutput = document.getElementById("ratingOutput");
	    ratingOutput.innerText = eventInfo.detail.tentativeRating;
	}

	app.start();
})();
