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
	
}
