function $(id) { return document.getElementById(id) };

window.onload = runCategories;

function runCategories() {

    //Click event for the four main categories: All, Top Selling, New Releases, & Recommendations
    var allcat = document.getElementsByClassName("allThreeCategories");
    for (let i = 0; i < allcat.length; i++) { allcat[i].onclick = showAllCategories; }

    var topSellingcat = document.getElementsByClassName("topSellingCategory");
    for (let i = 0; i < topSellingcat.length; i++) { topSellingcat[i].onclick = showTopSellingCategory; }

    var newRelcat = document.getElementsByClassName("newReleasesCategory");
    for (let i = 0; i < newRelcat.length; i++) { newRelcat[i].onclick = showNewReleasesCategory; }

    var recCat = document.getElementsByClassName("recommendationsCategory");
    for (let i = 0; i < recCat.length; i++) { recCat[i].onclick = showRecommendationsCategory; }

    //Change event for subcategories drop down
    document.getElementById("gamesSubcategories").onchange = changeSubcategory;

    //Click event for every small div - clickable but not functional for now
    var clickableSmallDivs = document.getElementsByClassName("smallestDivOfItem");
    for (let i = 0; i < clickableSmallDivs.length; i++) { clickableSmallDivs[i].onclick = getSmallDivInfo; }

    var listOfTitles = document.getElementsByClassName("title");
    var titletext;
    for (var i = 0; i < listOfTitles.length; i++) {
        titletext = listOfTitles[i].innerText;
        listOfTitles[i].title = titletext;
    }

    $("Search_Bar_Button").onclick = SearchForItem;
    $("Search_Bar_Field").oninput = SearchForItem;
    $("Currency").onchange = ChangeCurrency;



}


//Search For an item
function SearchForItem() {
    var typed_input = $("Search_Bar_Field").value;
    typed_input = typed_input.toLowerCase();
    if (typed_input != "") {

        //Now check which divs show and which get hidden

        //Check Top Selling Items
        var showTopSellingTitle = false; //needed to show/hide the 'No items found'
        var topSellingBiggestDiv = document.getElementsByClassName("topSellingTenItems")[0];
        var tenDivs = topSellingBiggestDiv.getElementsByClassName("smallestDivOfItem");

        for (let i = 0; i < tenDivs.length; i++) { //loop over the 10 divs
            var smallDiv = tenDivs[i];
            var smallDivTitle = smallDiv.getElementsByClassName("title")[0].innerText.toLowerCase();
            if (smallDivTitle.includes(typed_input)) { //check if input text is included
                smallDiv.style.display = "inline"; //then keep it
                showTopSellingTitle = true;
                document.getElementsByClassName("nogamesFound")[0].style.display = "none";
            }
            else {
                smallDiv.style.display = "none"; //hide it
            }
        }

        if (showTopSellingTitle == false) {
            //var bla = document.getElementsByClassName("nogamesFound")[0].innerHTML;
            //alert(bla);
            document.getElementsByClassName("nogamesFound")[0].style.display = "block";
            //document.getElementsByClassName("nogamesFound")[1].style.display = "none";
            //document.getElementsByClassName("nogamesFound")[2].style.display = "none";  
        }


        //Check New Releases items
        var showNewReleasesTitle = false;
        var newReleasesBiggestDiv = document.getElementsByClassName("newReleasesTenItems")[0];
        var tenDivs = newReleasesBiggestDiv.getElementsByClassName("smallestDivOfItem");

        for (let i = 0; i < tenDivs.length; i++) {
            var smallDiv = tenDivs[i];
            var smallDivTitle = smallDiv.getElementsByClassName("title")[0].innerText.toLowerCase();
            if (smallDivTitle.includes(typed_input)) {
                smallDiv.style.display = "inline";//then keep it
                showNewReleasesTitle = true;
                document.getElementsByClassName("nogamesFound")[1].style.display = "none";
            }
            else {
                smallDiv.style.display = "none";//hide it
            }
        }

        if (showNewReleasesTitle == false) {
            //document.getElementsByClassName("nogamesFound")[0].style.display = "none";
            document.getElementsByClassName("nogamesFound")[1].style.display = "block";
            //document.getElementsByClassName("nogamesFound")[2].style.display = "none"; 
        }


        //Check Recommendations items
        var showRecommendationsTitle = false;
        var recommendationsBiggestDiv = document.getElementsByClassName("recommendationsTenItems")[0];
        var tenDivs = recommendationsBiggestDiv.getElementsByClassName("smallestDivOfItem");

        for (let i = 0; i < tenDivs.length; i++) {
            var smallDiv = tenDivs[i];
            var smallDivTitle = smallDiv.getElementsByClassName("title")[0].innerText.toLowerCase();
            if (smallDivTitle.includes(typed_input)) {
                smallDiv.style.display = "inline";//then keep it
                showRecommendationsTitle = true;
                document.getElementsByClassName("nogamesFound")[2].style.display = "none";
            }
            else {
                smallDiv.style.display = "none";//hide it
            }
        }

        if (showRecommendationsTitle == false) {
            //document.getElementsByClassName("nogamesFound")[0].style.display = "none";
            //document.getElementsByClassName("nogamesFound")[1].style.display = "none";
            document.getElementsByClassName("nogamesFound")[2].style.display = "block";
        }

    }
    else { //all categories are needed
        var allSmallDivs = document.getElementsByClassName("smallestDivOfItem");

        for (let i = 0; i < allSmallDivs.length; i++) {
            allSmallDivs[i].style.display = "inline";
        }

        document.getElementsByClassName("nogamesFound")[0].style.display = "none";
        document.getElementsByClassName("nogamesFound")[1].style.display = "none";
        document.getElementsByClassName("nogamesFound")[2].style.display = "none";
    }


}
//End of function




function showAllCategories() { //show all 4 categories
    //alert("inAll");
    document.getElementsByClassName("newReleasesTenItems")[0].style.display = "inline";
    document.getElementsByClassName("topSellingTenItems")[0].style.display = "inline";
    document.getElementsByClassName("recommendationsTenItems")[0].style.display = "inline";

}

function showTopSellingCategory() { //show Top Selling
    //alert("inTopSelling");
    document.getElementsByClassName("newReleasesTenItems")[0].style.display = "none";
    document.getElementsByClassName("topSellingTenItems")[0].style.display = "inline";
    document.getElementsByClassName("recommendationsTenItems")[0].style.display = "none";

}

function showNewReleasesCategory() { //show New Releases 
    //alert("inNewReleases");
    document.getElementsByClassName("newReleasesTenItems")[0].style.display = "inline";
    document.getElementsByClassName("topSellingTenItems")[0].style.display = "none";
    document.getElementsByClassName("recommendationsTenItems")[0].style.display = "none";

}

function showRecommendationsCategory() { //show Recommendations
    //alert("inRecommendations");
    document.getElementsByClassName("newReleasesTenItems")[0].style.display = "none";
    document.getElementsByClassName("topSellingTenItems")[0].style.display = "none";
    document.getElementsByClassName("recommendationsTenItems")[0].style.display = "inline";

}

function changeSubcategory() { //change subcategory after user selects it

    var userSubCategory = document.getElementById("gamesSubcategories").value;

    if (userSubCategory != "") {

        //what we need to look for: 
        var weNeed;
        //adventureGame
        //actionGame
        //strategyGame
        //simulationGame
        //arcadeGame
        //sportsGame
        //boardGame
        if (userSubCategory == "Action") { weNeed = "actionGame"; } //e.g. 'Biography' is the dropdown's value, but biographyBook is the div's class
        if (userSubCategory == "Adventure") { weNeed = "adventureGame"; }
        if (userSubCategory == "Arcade") { weNeed = "arcadeGame"; }
        if (userSubCategory == "Sports") { weNeed = "sportsGame"; }
        if (userSubCategory == "Board") { weNeed = "boardGame"; }
        if (userSubCategory == "Simulation") { weNeed = "simulationGame"; }
        if (userSubCategory == "Strategy") { weNeed = "strategyGame"; }


        //Now check which divs show and which get hidden

        //Check Top Selling Items
        var showTopSellingTitle = false; //needed to show/hide the 'No items found'
        var topSellingBiggestDiv = document.getElementsByClassName("topSellingTenItems")[0];
        var tenDivs = topSellingBiggestDiv.getElementsByClassName("smallestDivOfItem");

        for (let i = 0; i < tenDivs.length; i++) { //loop over the 10 divs
            var smallDiv = tenDivs[i];
            var smallDivSubcategory = smallDiv.getElementsByClassName("categoryOfSmallestDivItem")[0];
            if (smallDivSubcategory.classList.contains(weNeed)) { //check its class
                smallDiv.style.display = "inline"; //then keep it
                showTopSellingTitle = true;
                document.getElementsByClassName("nogamesFound")[0].style.display = "none";
            }
            else {
                smallDiv.style.display = "none"; //hide it
            }
        }

        if (showTopSellingTitle == false) {
            //var bla = document.getElementsByClassName("nogamesFound")[0].innerHTML;
            //alert(bla);
            document.getElementsByClassName("nogamesFound")[0].style.display = "block";
            //document.getElementsByClassName("nogamesFound")[1].style.display = "none";
            //document.getElementsByClassName("nogamesFound")[2].style.display = "none";  
        }


        //Check New Releases items
        var showNewReleasesTitle = false;
        var newReleasesBiggestDiv = document.getElementsByClassName("newReleasesTenItems")[0];
        var tenDivs = newReleasesBiggestDiv.getElementsByClassName("smallestDivOfItem");

        for (let i = 0; i < tenDivs.length; i++) {
            var smallDiv = tenDivs[i];
            var smallDivSubcategory = smallDiv.getElementsByClassName("categoryOfSmallestDivItem")[0];
            if (smallDivSubcategory.classList.contains(weNeed)) {
                smallDiv.style.display = "inline";//then keep it
                showNewReleasesTitle = true;
                document.getElementsByClassName("nogamesFound")[1].style.display = "none";
            }
            else {
                smallDiv.style.display = "none";//hide it
            }
        }

        if (showNewReleasesTitle == false) {
            //document.getElementsByClassName("nogamesFound")[0].style.display = "none";
            document.getElementsByClassName("nogamesFound")[1].style.display = "block";
            //document.getElementsByClassName("nogamesFound")[2].style.display = "none"; 
        }


        //Check Recommendations items
        var showRecommendationsTitle = false;
        var recommendationsBiggestDiv = document.getElementsByClassName("recommendationsTenItems")[0];
        var tenDivs = recommendationsBiggestDiv.getElementsByClassName("smallestDivOfItem");

        for (let i = 0; i < tenDivs.length; i++) {
            var smallDiv = tenDivs[i];
            var smallDivSubcategory = smallDiv.getElementsByClassName("categoryOfSmallestDivItem")[0];
            if (smallDivSubcategory.classList.contains(weNeed)) {
                smallDiv.style.display = "inline";//then keep it
                showRecommendationsTitle = true;
                document.getElementsByClassName("nogamesFound")[2].style.display = "none";
            }
            else {
                smallDiv.style.display = "none";//hide it
            }
        }

        if (showRecommendationsTitle == false) {
            //document.getElementsByClassName("nogamesFound")[0].style.display = "none";
            //document.getElementsByClassName("nogamesFound")[1].style.display = "none";
            document.getElementsByClassName("nogamesFound")[2].style.display = "block";
        }

    }

    else { //all categories are needed
        var allSmallDivs = document.getElementsByClassName("smallestDivOfItem");

        for (let i = 0; i < allSmallDivs.length; i++) {
            allSmallDivs[i].style.display = "inline";
        }

        document.getElementsByClassName("nogamesFound")[0].style.display = "none";
        document.getElementsByClassName("nogamesFound")[1].style.display = "none";
        document.getElementsByClassName("nogamesFound")[2].style.display = "none";
    }
}


function ChangeCurrency() {
    var price_elements = document.getElementsByClassName("price");
    var price;
    var new_price;
    var price_array;
    if (this.value == "USD $") { //convert from LBP to USD
        for (var i = 0; i < price_elements.length; i++) {
            price = price_elements[i].innerText.toLowerCase();
            if (price != "free" && !price.includes("$")) {
                price_array = price.split(" ");
                price_elements[i].innerText = "$ " + (price_array[1] / 1515).toFixed(2);
            }

        }
    } else if (this.value == "LBP L.L") { //convert from USD to LBP
        for (var i = 0; i < price_elements.length; i++) {
            price = price_elements[i].innerText.toLowerCase();
            if (price != "free" && !price.includes("LBP")) {
                price_array = price.split(" ");
                price_elements[i].innerText = "LBP " + Math.ceil(price_array[1]*1515);
            }

        }
    }


}



function getSmallDivInfo() {
    //alert("click");
    return; //for now
}