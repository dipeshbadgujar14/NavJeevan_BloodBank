from django.urls import path

from HelpAFriend import views 

urlpatterns = [
		path('auth',views.Auth_User),
		path('registration',views.Registration_User),
		path('login',views.Login_User),
		path('submit',views.Submit),
		path('',views.Index),
		path('search',views.Search_Page),
		path('search_donor',views.Search_Donor),
		path('post_request',views.Post_Request),
		path('post_req',views.Post_Req),
		path('search_bank',views.Bank_List),
		path('bloodbank_registration',views.BloodBank_Registration),
		path('submit_bloodbank',views.Submit_BloodBank),
		path('bloodbank_details',views.BloodBank_Details),
		path('update_units',views.Update_Units),
		path('edit_profile',views.Edit_Profile),
		path('update_details',views.Update_Details),
		path('user_home',views.User_Home),
		path('change_password',views.Change_Password),
		path('change_pass',views.Change_Pass),
		path('logout',views.Logout),
		path('edit_bb_profile',views.Edit_BB_Profile),
		path('update_bb_details',views.Update_BB_Details),
		path('bloodbank_home',views.BloodBank_Home),
		path('forgot_password',views.Forgot_Password),
		path('new_password',views.New_Password),
		path('enter_otp',views.Enter_Otp),
		path('generate_otp',views.Generate_Otp),
		path('verify_otp',views.Verify_Otp),
		path('update_password',views.Update_Password),
		path('aboutus',views.AboutUS),
	]

