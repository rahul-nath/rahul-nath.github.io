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
    var names = ['Medicost', 'Honors Senior Research','Queuer','Virtual Assembly Emulation']; // Laundry List App
    var pictures = ["images/medicost.jpg", "images/dfa.png", "images/androiddev.jpg", "images/assembly.png"];

    projects['Medicost'] = 'When I learned about them, I liked to do hackathons in college. Medicost is my project from the MIT Hacking Medicine Hackathon, designed to make it easy to look up the cost of a medical procedure by doctors accepting Medicare and Medicaid. For those without insurance, it is often difficult to anticipate the cost of expensive treatments until it is too late. This website allows such individuals to see the cost requests made by doctors to insurance companies and how much they received as a result of their requests, along with other information regarding the doctor\'s practice. Data was scraped from the Dept. of Health and Human services.';
    projects['Honors Senior Research'] = '<i>Learning Domain Models from Partially Observed Action Sequences: <a href="https://github.com/rahul-nath/PrePost2/blob/master/final_try.py" target="_blank">PrePost2</a></i>.  For an honors senior project, I continued <b>natural language processing</b> research I had started at the <b>Naval Research Lab</b>. I worked on extending extant algorithms that learn action models from partially-observed intermediate state information to learn models from sparse descriptions of action sequences. I was trying to facilitate closed knowledge loop automation by using transfer learning to "fill in" missing information about the environment. Inputs included domain information and action sequences to discover static predicates for the actions. It employs parallel processing, web scraping, and Supervised Machine Learning.';
    projects['Queuer'] = 'I had a great internship in Android Development, integrating hardware tech with Android apps. In June 2014 I gave a talk at the AnDevCon conference in Boston on Google Glass, iBeacons, and Android applications. I\'ve also developed an Android application called <strong>Queuer</strong> that allows people to keep track of different tasks they have to do and allows them to manage their completion. It utilizes Android tools such as <b>Volley, GSON</b>, and the <b>SQLite</b> database. I worked in conjunction with a team and the code is available on my Github account.';
    projects['Virtual Assembly Emulation'] = 'I wrote a virtual emulator for a RISC assembly instruction set, WARM, using a CISC assembly instruction set, WIND, to better understand the hardware instruction set emulation efficiency tradeoffs that occur when CISC instruction sets like x86 attempt to emulate RISC instruction sets, like ARM. WARM is a language similar to the ARM instruction set and WIND resembles Intel x86-64 instruction set. The project was a lot of fun (and work), and gave me detailed insight into what goes on under the hood and in the hardware of a machine.';
    //projects['Laundry List App'] = 'Helps to create a list of clothes worn in the past week so users know how long it has been worn. Intended for college students.';

    ec['WSO'] = 'At Williams I was on the executive board of Williams Students Online, a student resource <a href="http://wso.williams.edu" target="_blank">website</a> established in 1995 to connect the Williams student body in ways hitherto unimagined; creating a unified Facebook profile for each student at Williams, providing a Lost+Found, an exchange forum, a student body discussion forum, and a ride offering forum among other networking services. The framework used for the site is Ruby on Rails.';
    ec['WCFM'] = 'I also served as webmaster on the executive board of <a href="http://wcfm.williams.edu" target="_blank">WCFM</a>, Williams College\'s student-run radio station. I would manage the blog, automate logistical services like subrequests and scheduling, and share my musical interests with the greater Williams community. In addition to being a radio DJ, I was also a campus DJ, playing gigs for school dances and private parties alike. Check out the link to my soundcloud below.';
    ec['The Williams Octet'] = 'In college I loved to sing. I was part of <a href="http://williamsoctet.com" target="_blank">The Williams Octet</a>, Williams\' oldest all-male a capella group, dating back to 1940. We sang for a variety of different charity events and fundraisers, including one that I started my freshman year called "Pay it Ephward" -- a silent auction dedicated to raising money for food kitchens in nearby North Adams.';
    ec['Williams Strength Club'] = 'While at Williams, I co-founded Williams Strength: Williams\' first student-run weightlifting organization devoted to serving the non-athletes and club athletes. We would help new lifters get acquainted with the weightroom and a variety of different workout routines, such as bodybuilding and olympic lifting.';
    // on click, fade out the nodes of $(#projects)

    $('#heading').replaceWith('<h2 id="heading">' + names[i%names.length] + '</h2>');
    $("#text_desc").replaceWith('<p1 id="text_desc">' + projects[names[i%names.length]] + '</p1>');
    $('#ec-head').replaceWith('<h2 id="ec-head">' + ec_names[j%ec_names.length] + '</h2>');
    $("#ec-desc").replaceWith('<p1 id="ec-desc">' + ec[ec_names[j%ec_names.length]] + '</p1>');

    $('#the-arrow').click(function(){
      // need a callback for each fadeout where you make the change and then fadein
      $('#projects').fadeOut(500, function(){
        $('#heading').replaceWith('<h2 id="heading">' + names[i%names.length] + '</h2>');
        $("#text_desc").replaceWith('<p1 id="text_desc">' + projects[names[i%names.length]] + '</p1>');
        $('#projects').css("background-image", "url(" + pictures[i%names.length] + ")").fadeIn('slow');
      });

      if(i == names.length) i = 1;
      else i += 1;
      return false;
    });

    $('#ec-arrow').click(function(){
      // need a callback for each fadeout where you make the change and then fadein
      $('#activities').fadeOut(500, function(){
        $('#ec-head').replaceWith('<h2 id="ec-head">' + ec_names[j%ec_names.length] + '</h2>');
        $("#ec-desc").replaceWith('<p1 id="ec-desc">' + ec[ec_names[j%ec_names.length]] + '</p1>');
        $('#activities').css("background-image", "url(" + ec_pics[j%ec_names.length] + ")").fadeIn('slow');
      });

      if(j == ec_names.length) j = 1;
      else j += 1;
      return false;
    });
});
