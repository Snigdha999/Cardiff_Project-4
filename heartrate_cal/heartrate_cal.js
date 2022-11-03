function SymError()
{
  return true;
}

window.onerror = SymError;

var SymRealWinOpen = window.open;

function SymWinOpen(url, name, attributes)
{
  return (new Object());
}

window.open = SymWinOpen;


   

function ClearForm(form){



    form.age.value = ""; 

    form.rhr.value = "";

    form.mhr.value = "";

	form.fifty.value = ""; form.AR50.value = "";

	form.fiftyfive.value = ""; form.AR55.value = "";

	form.sixty.value = ""; form.AR60.value = "";

	form.sixtyfive.value = ""; form.AR65.value = "";

	form.seventy.value = ""; form.AR70.value = "";

	form.seventyfive.value = ""; form.AR75.value = "";

	form.eighty.value = ""; form.AR80.value = "";

	form.eightyfive.value = "";  form.AR85.value = "";

	form.ninety.value = ""; form.AR90.value = "";

	form.ninetyfive.value = ""; form.AR95.value = "";


}



function mhr(age, rhr) {



         ageindx=(220-age);

          return ageindx;
			
			
			

}



function checkform(form) {



       if (form.age.value==null){

            alert("\nPlease complete the form first");

            return false;

       }



       else if  (parseFloat(form.rhr.value) <= 0||

					parseFloat(form.rhr.value) >=101||

                parseFloat(form.age.value) <=14||

                parseFloat(form.age.value) >=101){

                alert("\nOne of the values is incorrect. Please enter the values again.");

                ClearForm(form);

                return false;

       }

       return true;



}



function computeform(form) {



       if (checkform(form)) {

 	
		yourmhr=Math.round(mhr(form.age.value/1));
		
		form.mhr.value=yourmhr;
		var resthr=form.rhr.value;
		var adjhr=(form.mhr.value-form.rhr.value);
		form.AR50.value=Math.round(yourmhr*0.50);
		form.AR55.value=Math.round(yourmhr*0.55);
		form.AR60.value=Math.round(yourmhr*0.60);
		form.AR65.value=Math.round(yourmhr*0.65);
		form.AR70.value=Math.round(yourmhr*0.70);
		form.AR75.value=Math.round(yourmhr*0.75);
		form.AR80.value=Math.round(yourmhr*0.80);
		form.AR85.value=Math.round(yourmhr*0.85);
		form.AR90.value=Math.round(yourmhr*0.90);
		form.AR95.value=Math.round(yourmhr*0.95);

    	form.fifty.value=Math.round((adjhr*0.50)+(resthr*1));
		form.fiftyfive.value=Math.round((adjhr*0.55)+(resthr*1));
		form.sixty.value=Math.round((adjhr*0.60)+(resthr*1));
		form.sixtyfive.value=Math.round((adjhr*0.65)+(resthr*1));
		form.seventy.value=Math.round((adjhr*0.70)+(resthr*1));
		form.seventyfive.value=Math.round((adjhr*0.75)+(resthr*1));
		form.eighty.value=Math.round((adjhr*0.80)+(resthr*1));
		form.eightyfive.value=Math.round((adjhr*0.85)+(resthr*1));
		form.ninety.value=Math.round((adjhr*0.90)+(resthr*1));
		form.ninetyfive.value=Math.round((adjhr*0.95)+(resthr*1));


		
		return;

		form.mhr.value=yourmhr;
		var resthr=form.rhr.value;
		var adjhr=((form.mhr.value-form.rhr.value)*(0.60));
    	form.fifty.value=((adjhr*1) + (resthr*1));

	
     }
       return;

}




