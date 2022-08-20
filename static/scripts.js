$(document).ready(function() {
    setInterval("update_values()",1000); // call every 1 second
});

function update_values() { 
    $.getJSON("/update_data",
        function(data) {
            $("#temp_o").text(data.o_temp)
            $("#humi_o").text(data.o_humi)
            $("#pressure_o").text(data.o_pressure)
            $("#battery_o").text(data.o_battery)
            $("#updatetime_o").text(data.o_updatet)
            $("#temp_m").text(data.m_temp)
            $("#humi_m").text(data.m_humi)
            $("#pressure_m").text(data.m_pressure)
            $("#battery_m").text(data.m_battery)
            $("#updatetime_m").text(data.m_updatet)
        });
  }


//$( document ).ready(function() {
//    function update_values() {
//        $.getJSON("127.0.0.1/update_data",
//            function(data) {
//                $("#temp_o").text(data.o_temp)
//            });
//    }
//});