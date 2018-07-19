odoo.define('rfid.filter_button', function (require) {

"use strict";

var core = require('web.core');

var ListController = require('web.ListController');

    ListController.include({

        renderButtons: function($node) {

        this._super.apply(this, arguments);

            if (this.$buttons) {

                let filter_button = this.$buttons.find('.invoke_API'); //same with the button class in qweb.xml

                filter_button && filter_button.click(this.proxy('filter_button')) ;

            }

        },

        filter_button: function () {

            console.log('yay filter')
            console.log('Invoke API')

               var xhttp = new XMLHttpRequest();
               var api_url = "https://rfidindonesia.intellifi.nl/api/presences?key=9d0c13dc-fef4-4b94-af88-8bd237b628d7";
               xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                 console.log(this.responseText);
                }
              };
                xhttp.open("GET", api_url, true);
                  xhttp.send();
              //implement your click logic here


        }

    });

})