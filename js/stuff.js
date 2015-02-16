// initialize hash map here
// if there isn't a hashmap (unlikely), make two arrays


$(document).ready(function(){
    // the equivalent of show and hide 
    var i = 0;
    var j = 0;
    var projects = {};
    var ec = {};
    var ec_names = ['WSO', 'WCFM', 'The Williams Octet', 'Williams Strength Club'];
    var ec_pics = ["images/wso.png", "images/wcfm.jpg", "images/octet.jpg", "images/williams_strength.jpg"];
    var names = ['Medicost','Senior Honors Research','Virtual Assembly Emulation','Queuer']; // Laundry List App
    var pictures = ["images/medicost.jpg", "images/dfa.png", "images/assembly.png", "images/queuer.png"];
    
    projects['Medicost'] = 'A MIT Hacking Medicine Hackathon project designed to make it easy to look up the cost of a medical procedure by doctors accepting Medicare and Medicaid. For those without insurance, it is often difficult to anticipate the cost of expensive treatments until it is too late. My website allows such individuals to see the cost requests made by doctors to insurance companies and how much they received as a result of their requests, along with other information regarding the doctor\'s practice. Data was taken from the depths of the Dept. of Health and Human services website.';
    projects['Senior Honors Research'] = '<i>Learning Domain Models from Partially Observed Action Sequences</i>. I performed research on extending extant algorithms that learn action models from partially observed intermediate state information to learning models from sparse descriptions of action sequences. My goal was to find a way to facilitate closed knowledge loop automation by using the Internet to "fill in" missing information about the environment given information about the domain and the aforementioned action sequences to discover static predicates for the actions.';
    projects['Virtual Assembly Emulation'] = 'I wrote a virtual emulator for a RISC assembly instruction set, WARM, using a CISC assembly instruction set, WIND, to better understand the hardware limitations of actual instruction set emulation that occurs when CISC instruction sets like x86 attempt to emulate RISC instruction sets, like ARM. WARM is a language similar to the ARM instruction set and WIND resembles Intel x86-64 instruction set. The project was a lot of fun (and work), and gave me detailed insight into what goes on under the hood and in the hardware of a machine.';
    projects['Queuer'] = 'Developed an Android application called <strong>Queuer</strong> that allows people to keep track of different tasks they have to do and allows them to manage their completion. It utilizes Android tools such as Volley, GSON, and the SQLite database and was developed using the AGILE methodology. I worked in conjunction with a team and the code is readily available on my Github account, as are select other projects included in my showcase of projects here. The app itself is not for sale (saturated marketplace), but it was a great way to get my feet wet in app development.';
    //projects['Laundry List App'] = 'Helps to create a list of clothes worn in the past week so users know how long it has been worn. Intended for college students.';

    ec['WSO'] = 'I am on the executive board of Williams Students Online, a student resource <a href="http://wso.williams.edu">website</a> established in 1995 to connect the Williams student body in ways hitherto unimagined; creating a unified Facebook profile for each student at Williams, providing a Lost+Found, an exchange forum, a student body discussion forum, and a ride offering forum among other networking services. The framework used for the site is Ruby on Rails.';
    ec['WCFM'] = 'I currently serve as webmaster on the executive board of <a href="http://wcfm.williams.edu">WCFM</a>, Williams College\'s student-run radio station. I post on the blog, automate logistical services like subrequests and scheduling, and share my musical interests with the greater Williams community. Check out the link to my soundcloud below.';
    ec['The Williams Octet'] = 'Coming into college I loved to sing, so I tried out and was accepted by The Octet, Williams\' oldest all-male a capella group, dating back to 1940. We sing for a variety of different charity events and fundraisers, including one that I started my freshman year called "Pay it Ephward", a silent auction dedicated to raising money for food kitchens in nearby North Adams.';
    ec['Williams Strength Club'] = 'This year I co-founded Williams Strength: Williams\' first student-run weightlifting organization devoted to serving the non-athletes and club athletes at Williams College. We meet three times a week for an hour where we help new lifters get acquainted with the weightroom and a variety of different workout routines, such as bodybuilding and olympic lifting.';
    // on click, fade out the nodes of $(#projects)

    $('#heading').replaceWith('<h1 id="heading">' + names[i%names.length] + '</h1>');
    $("#text_desc").replaceWith('<p1 id="text_desc">' + projects[names[i%names.length]] + '</p1>');
    i+= 1;
    //var v = $('#picture').attr('src');
    //console.log(v);

    // iterate to the next key-value in hashmap
    $('#the-arrow').click(function(){
      // need a callback for each fadeout where you make the change and then fadein
      $('#heading').replaceWith('<h1 id="heading">' + names[i%names.length] + '</h1>');
      //$('#heading').fadeIn(3000).delay(1000).fadeOut(10000);
      $("#text_desc").replaceWith('<p1 id="text_desc">' + projects[names[i%names.length]] + '</p1>');
      //$("#text_desc").fadeIn(3000).delay(1000).fadeOut(10000);

      $('#picture').attr('src', pictures[i%names.length]);
      var newpic = $('#picture').attr('src');
      console.log(newpic);
      if(i == names.length) i = 1;
      else i += 1;
      return false;
    });

    $('#ec-head').replaceWith('<h1 id="ec-head">' + ec_names[j%ec_names.length] + '</h1>');
    $("#ec-desc").replaceWith('<p1 id="ec-desc">' + ec[ec_names[j%ec_names.length]] + '</p1>');
    j+= 1;
    $('#ec-arrow').click(function(){
      // need a callback for each fadeout where you make the change and then fadein
      $('#ec-head').replaceWith('<h1 id="ec-head">' + ec_names[j%ec_names.length] + '</h1>');
      //$('#heading').fadeIn(3000).delay(1000).fadeOut(10000);
      $("#ec-desc").replaceWith('<p1 id="ec-desc">' + ec[ec_names[j%ec_names.length]] + '</p1>');
      //$("#text_desc").fadeIn(3000).delay(1000).fadeOut(10000);

      $('#ec-pic').attr('src', ec_pics[j%ec_names.length]);
      var newpic = $('#ec-pic').attr('src');
      console.log(newpic);
      if(j == ec_names.length) j = 1;
      else j += 1;
      return false;
    });
});

    //while(1){

        // for loop here for the hashmap

            // section id is 'two'
            // put the text into a hashmap; value is the text, key is the organization
            // go through each element in the array
            // replace id 'heading' with the key, id 'text_desc' with the value
            // pause for 20 seconds
            // move on to the next description

            // use the class id of "projects"

            // for each child node of $(projects)
            // arrow functionality to move to next iteration of loop
            // fuck it, just do the arrow and advance on click.

/*
            (function myLoop (i) {          
                setTimeout(function () { 
                  for(var d in projects){
                    console.log(d);  
                    $('#heading').fadeOut(5000, function() {
                        $(this).replaceWith('<h2 id="heading">' + d + '</h2>', function() {
                            $(this).fadeIn(1000);
                            $("#text_desc").replaceWith('<p1 id="text_desc">' + projects[d] + '</p1>');
                            var head = $(this);
                            var desc = $("#text_desc")
                            setTimeout(function() { 
                              head.delay(5000).fadeOut(1000);
                              desc.delay(5000).fadeOut(1000);
                            }, 1000);
                        }));
                    }); 
                    if (--i) myLoop(i, d);      //  decrement i and call myLoop again if i > 0
                  }

                }, 3000);
            })(10);                //  pass the number of iterations as an argument
                //$("#heading").replaceWith('<h2 id="heading">' + d + '</h2>');


var i = 1;                     //  set your counter to 1

function myLoop () {           //  create a loop function
   setTimeout(function () {    //  call a 3s setTimeout when the loop is called
      alert('hello');          //  your code here
      i++;                     //  increment the counter
      if (i < 10) {            //  if the counter < 10, call the loop function
         myLoop();             //  ..  again which will trigger another 
      }                        //  ..  setTimeout()
   }, 3000)
}
*/

              //clearTimeout(timeout);

           //$("#text_desc")[0].delay(10000).fadeout(400);
           //make an arrow icon using font awesome
           // make id. if clicked, continue
           //$("arrow").click(function(){
           //    continue;
           // });

    //}
