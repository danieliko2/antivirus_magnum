//     $(function() {
//         $('a#list_ips').on('click', function(e){
//             $.ajax({
//                 url: '',
//                 type: 'get',
//                 contentType: 'application/json',
//                 "id": "getIp",
//                 data: {
//                     list_ips_txt: $(this).innerHTML,
//                     test_text: "test"
//                 },
//                 success: function(response){
//                     document.getElementById("ips").innerHTML = response.ip
//                 }
//             })
//             console.log("clicked")
            
//         })
//     });

//    function addIP(){
//     $.ajax({
//         url: '',
//         type: 'get',
//         contentType: 'application/json',
//         "id": "addIP",
//         data: {
//             ip: document.getElementById("ipAdr").innerText,
//             riskN: document.getElementById("riskN").innerText,
//             comments: document.getElementById("comment").innerText
//         },
//         success: function(response){
//             document.getElementById("ips").innerHTML = "ip added"
//         }
//     })
//    }

$(document).ready(function(){ 
    console.log("mainscript up");

    document.getElementById("listen_submit").addEventListener("click", function() {
        console.log("updating listen");
        document.getElementById("ip_list").style.display="block";
        document.getElementById("ip_scan_spinner").style.display="block";  
    });

});






