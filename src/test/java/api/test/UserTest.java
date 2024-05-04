package api.test;

import org.junit.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import com.github.javafaker.Faker;
import io.restassured.response.*;
import api.endpoints.UserEndpoints;
import api.payload.User;


public class UserTest {

	
	Faker faker;
	User userPayload;
	
	@BeforeClass
	public void setupData() {
	
		faker = new Faker();
		userPayload= new User();
		
		userPayload.setId(faker.idNumber().hashCode());
		userPayload.setEmail(faker.internet().safeEmailAddress());
		userPayload.setFirstname(faker.name().firstName());
		userPayload.setLastname(faker.name().lastName());
		userPayload.setUsername(faker.name().username());
		userPayload.setPassword(faker.internet().password(5,10));
		userPayload.setPhone(faker.phoneNumber().cellPhone());
		
	}
	
	
	@Test(priority = 1)
	public void testPostUser() {
	
		Response response = UserEndpoints.createUser(userPayload);
		response.then().log().all();
		Assert.assertEquals(response.getStatusCode(),200);
		
	}
	
	@Test(priority = 2)
	public void testGetUserByName() {
		
		Response response = UserEndpoints.readUser(this.userPayload.getUsername());
		response.then().log().all();
		//getStatus code used in assertion and .statuscode give 200 directly
		Assert.assertEquals(response.getStatusCode(),200);
		
	}

	
	@Test(priority = 3)
	public void testUpdateUserByName() {
		//update data using payload
		
		userPayload.setEmail(faker.internet().safeEmailAddress());
		userPayload.setFirstname(faker.name().firstName());
		userPayload.setLastname(faker.name().lastName());
		
		
		Response response = UserEndpoints.updateUser(this.userPayload.getUsername(),userPayload);
		//chai assertion 
		response.then().log().body().statusCode(200);
		response.then().log().all();
		response.then().log().body();
		//testng assertion
		Assert.assertEquals(response.getStatusCode(),200);
		//checking data after updation
		
		Response responseafterupdate = UserEndpoints.readUser(this.userPayload.getUsername());
		responseafterupdate.then().log().all();
		responseafterupdate.then().log().body();
		Assert.assertEquals(responseafterupdate.getStatusCode(),200);
		
		
	}
	@Test(priority = 4)
	public void testDeleteUserName() {
		
		Response response = UserEndpoints.deleteUser(this.userPayload.getUsername());
		Assert.assertEquals(response.getStatusCode(),200);
		
	}

	
	
}
