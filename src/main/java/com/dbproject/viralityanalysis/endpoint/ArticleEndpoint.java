package com.dbproject.viralityanalysis.endpoint;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.TimeUnit;

import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

import com.dbproject.viralityanalysis.entity.Article;
import com.google.appengine.repackaged.com.google.gson.Gson;
import com.google.gson.JsonParser;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

/**
 * Endpoints for User.
 */
@Path("api/article")
public class ArticleEndpoint {

	/**
	 * Enters all the records from the csv to the ES datastore.
	 * @return The count of records that are saved to ES.
	 * @throws IOException 
	 * @throws InterruptedException 
	 */
	@POST
	@Path("train")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	public String saveArticlesES() throws IOException, InterruptedException {
		
		int i=1;

		String csvFile = "WEB-INF/OnlineNewsPopularity.csv";
		BufferedReader br = null;
		String line = "";
		String cvsSplitBy = ",";
		
		Double avgGlobalSubjectivity = 0.0;
		Double avgGlobalSentimentPolarity = 0.0;
		Double avgRatePositiveWords = 0.0;
		Double avgRateNegativeWords = 0.0;
		Double avgTitleSubjectivity = 0.0;
		Double avgTitleSentimentPolarity = 0.0;
		
		Double avgImagesNumber = 0.0;
		Double avgVideosNumber = 0.0;
		Double avgLinksNumber = 0.0;
		Double avgKeywords = 0.0;
		
		Double sharesLessThanHundred = 0.0;
		Double sharesHundredToThousand = 0.0;
		Double sharesThousandToTenThousand = 0.0;
		Double sharesGreaterThanTenThousand = 0.0;
		
		Double dayMonday = 0.0;
		Double dayTuesday = 0.0;
		Double dayWednesday = 0.0;
		Double dayThursday = 0.0;
		Double dayFriday = 0.0;
		Double daySaturday = 0.0;
		Double daySunday = 0.0;
		
		Double categoryLifestyle = 0.0;
		Double categoryEntertainment = 0.0;
		Double categoryTech = 0.0;
		Double categorySocMed = 0.0;
		Double categoryBus = 0.0;
		Double categoryWorld = 0.0;
		
		
		br = new BufferedReader(new FileReader(csvFile));

		while ((line = br.readLine()) != null) {

			if(i==1){
				i++;
				continue;
			}
				
			// use comma as separator
			String[] articleMetaData = line.split(cvsSplitBy);
			Map<String,String> map = new HashMap<>();
			HttpClient client = HttpClientBuilder.create().build();
			String url = "http://localhost:9200/mashable/article/"+i;
			HttpPost post = new HttpPost(url);

			map.put("timedelta", articleMetaData[1]);
			map.put("nTokensTitle",articleMetaData[2]);
			map.put("nTokensContent", articleMetaData[3]);
			map.put("nUniqueTokens", articleMetaData[4]);
			map.put("nNonStopWords", articleMetaData[5]);
			map.put("nNonStopUniqueTokens", articleMetaData[6]);
			
			map.put("linksNumber", articleMetaData[7]);
			avgLinksNumber+=Double.valueOf(articleMetaData[7]);
			
			map.put("numSelfHrefs", articleMetaData[8]);
			
			map.put("imagesNumber", articleMetaData[9]);
			avgImagesNumber+=Double.valueOf(articleMetaData[9]);
			
			map.put("videosNumber", articleMetaData[10]);
			avgVideosNumber+=Double.valueOf(articleMetaData[10]);
			
			map.put("averageTokenLength", articleMetaData[11]);
			
			map.put("keywords", articleMetaData[12]);
			avgKeywords+=Double.valueOf(articleMetaData[12]);
			
			map.put("dataChannelIsLifestyle", articleMetaData[13]);
			categoryLifestyle+=Double.valueOf(articleMetaData[13]);
			
			map.put("dataChannelIsEntertainment", articleMetaData[14]);
			categoryEntertainment+=Double.valueOf(articleMetaData[14]);
			
			map.put("dataChannelIsBus", articleMetaData[15]);
			categoryBus+=Double.valueOf(articleMetaData[15]);
			
			map.put("dataChannelIsSocMed", articleMetaData[16]);
			categorySocMed+=Double.valueOf(articleMetaData[16]);
			
			map.put("dataChannelIsTech", articleMetaData[17]);
			categoryTech+=Double.valueOf(articleMetaData[17]);
			
			map.put("dataChannelIsWorld", articleMetaData[18]);
			categoryWorld+=Double.valueOf(articleMetaData[18]);
			
			map.put("kwMinMin", articleMetaData[19]);
			map.put("kwMaxMin", articleMetaData[20]);
			map.put("kwAvgMin", articleMetaData[21]);
			map.put("kwMinMax", articleMetaData[22]);
			map.put("kwMaxMax", articleMetaData[23]);
			map.put("kwAvgMax", articleMetaData[24]);
			map.put("kwMinAvg", articleMetaData[25]);
			map.put("kwMaxAvg", articleMetaData[26]);
			map.put("kwAvgAvg", articleMetaData[27]);
			map.put("minArticleShare", articleMetaData[28]);
			map.put("maxArticleShare", articleMetaData[29]);
			map.put("avgshareArticleShare", articleMetaData[30]);
			
			map.put("weekdayIsMonday", articleMetaData[31]);
			dayMonday+=Double.valueOf(articleMetaData[31]);
			
			map.put("weekdayIsTuesday", articleMetaData[32]);
			dayTuesday+=Double.valueOf(articleMetaData[32]);
			
			map.put("weekdayIsWednesday", articleMetaData[33]);
			dayWednesday+=Double.valueOf(articleMetaData[33]);
			
			map.put("weekdayIsThursday", articleMetaData[34]);
			dayThursday+=Double.valueOf(articleMetaData[34]);
			
			map.put("weekdayIsFriday", articleMetaData[35]);
			dayFriday+=Double.valueOf(articleMetaData[35]);
			
			map.put("weekdayIsSaturday", articleMetaData[36]);
			daySaturday+=Double.valueOf(articleMetaData[36]);
			
			map.put("weekdayIsSunday", articleMetaData[37]);
			daySunday+=Double.valueOf(articleMetaData[37]);
			
			map.put("isWeekend", articleMetaData[38]);
			map.put("LDA00", articleMetaData[39]);
			map.put("LDA01", articleMetaData[40]);
			map.put("LDA02", articleMetaData[41]);
			map.put("LDA03", articleMetaData[42]);
			map.put("LDA04", articleMetaData[43]);
			
			map.put("globalSubjectivity", articleMetaData[44]);
			avgGlobalSubjectivity+=Double.valueOf(articleMetaData[44]);
			
			map.put("globalSentimentPolarity", articleMetaData[45]);
			avgGlobalSentimentPolarity+=Double.valueOf(articleMetaData[45]);
			
			map.put("globalRatePositiveWords", articleMetaData[46]);
			map.put("globalRateNegativeWords", articleMetaData[47]);
			
			map.put("ratePositiveWords", articleMetaData[48]);
			avgRatePositiveWords+=Double.valueOf(articleMetaData[48]);
			
			map.put("rateNegativeWords", articleMetaData[49]);
			avgRateNegativeWords+=Double.valueOf(articleMetaData[49]);
			
			map.put("avgPositivePolarity", articleMetaData[50]);
			map.put("minPositivePolarity", articleMetaData[51]);
			map.put("maxPositivePolarity", articleMetaData[52]);
			map.put("avgNegativePolarity", articleMetaData[53]);
			map.put("minNegativePolarity", articleMetaData[54]);
			map.put("maxNegativePolarity", articleMetaData[55]);
			
			map.put("titleSubjectivity", articleMetaData[56]);
			avgTitleSubjectivity+=Double.valueOf(articleMetaData[56]);
			
			map.put("titleSentimentPolarity", articleMetaData[57]);
			avgTitleSentimentPolarity+=Double.valueOf(articleMetaData[57]);
			
			map.put("absTitleSubjectivity", articleMetaData[58]);
			map.put("absTitleSentimentPolarity", articleMetaData[59]);
			
			map.put("shares", articleMetaData[60]);
			Double noOfShares = Double.valueOf(articleMetaData[60].toString().trim());
			
			if(noOfShares<100)
				sharesLessThanHundred++;
			if(noOfShares>100 && noOfShares<1000)
				sharesHundredToThousand++;
			if(noOfShares>1000 && noOfShares<10000)
				sharesThousandToTenThousand++;
			if(noOfShares>10000)
				sharesGreaterThanTenThousand++;
			
//			try {
//				StringEntity se = new StringEntity(new Gson().toJson(map));
//				post.setEntity(se);
//				post.setHeader("Content-type", "application/json");
//				HttpResponse response = client.execute(post);
//				System.out.println(response);
//			} catch (ClientProtocolException e) {
//				System.out.println("ClientProtocol Exception");
//				e.printStackTrace();
//			} catch (IOException e) {
//				System.out.println("IOS Exception");
//				e.printStackTrace();
//			}

			i++;
			
//			if(i%3000==0)
//				TimeUnit.SECONDS.sleep(2);
		}
		
		
		br.close();
		
		
		Map<String,String> responseMap = new HashMap<>();
		
		responseMap.put("avgGlobalSubjectivity",String.valueOf((avgGlobalSubjectivity/i)));
		responseMap.put("avgGlobalSentimentPolarity",String.valueOf((avgGlobalSentimentPolarity/i)));
		responseMap.put("avgRateNegativeWords",String.valueOf((avgRateNegativeWords/i)));
		responseMap.put("avgRatePositiveWords",String.valueOf((avgRatePositiveWords/i)));
		responseMap.put("avgTitleSubjectivity",String.valueOf((avgTitleSubjectivity/i)));
		responseMap.put("avgTitleSentimentPolarity",String.valueOf((avgTitleSentimentPolarity/i)));
		
		responseMap.put("avgImagesNumber",String.valueOf((avgImagesNumber/i)));
		responseMap.put("avgVideosNumber",String.valueOf((avgVideosNumber/i)));
		responseMap.put("avgLinksNumber",String.valueOf((avgLinksNumber/i)));
		responseMap.put("avgKeywords",String.valueOf((avgKeywords/i)));
		
		responseMap.put("sharesLessThanHundred",String.valueOf((sharesLessThanHundred)));
		responseMap.put("sharesHundredToThousand",String.valueOf((sharesHundredToThousand)));
		responseMap.put("sharesThousandToTenThousand",String.valueOf((sharesThousandToTenThousand)));
		responseMap.put("sharesGreaterThanTenThousand",String.valueOf((sharesGreaterThanTenThousand)));
		
		responseMap.put("dayFriday",String.valueOf((dayFriday)));
		responseMap.put("dayMonday",String.valueOf((dayMonday)));
		responseMap.put("dayTuesday",String.valueOf((dayTuesday)));
		responseMap.put("dayWednesday",String.valueOf((dayWednesday)));
		responseMap.put("dayThursday",String.valueOf((dayThursday)));
		responseMap.put("daySaturday",String.valueOf((daySaturday)));
		responseMap.put("daySunday",String.valueOf((daySunday)));
		
		responseMap.put("categoryBus",String.valueOf((categoryBus)));
		responseMap.put("categoryEntertainment",String.valueOf((categoryEntertainment)));
		responseMap.put("categoryLifestyle",String.valueOf((categoryLifestyle)));
		responseMap.put("categorySocMed",String.valueOf((categorySocMed)));
		responseMap.put("categoryTech",String.valueOf((categoryTech)));
		responseMap.put("categoryWorld",String.valueOf((categoryWorld)));		
		
		
		responseMap.put("Response",(i-1)+" number of records pushed to ElasticSearch Index \"articles\" into type \"mashable\"");
		return new Gson().toJson(responseMap);
	}
	
	@SuppressWarnings("unused")
	private String getDay(String[] articleMetaData)
	{
		if(articleMetaData[31].equals("1"))
			return "Monday";
		if(articleMetaData[32].equals("1"))
			return "Tuesday";
		if(articleMetaData[33].equals("1"))
			return "Wednesday";
		if(articleMetaData[34].equals("1"))
			return "Thursday";
		if(articleMetaData[35].equals("1"))
			return "Friday";
		if(articleMetaData[36].equals("1"))
			return "Saturday";
		if(articleMetaData[37].equals("1"))
			return "Sunday";
		
		return "";
	}
	
	@SuppressWarnings("unused")
	private String getCategory(String[] articleMetaData)
	{
		if(articleMetaData[13].equals("1"))
			return "Lifestyle";
		if(articleMetaData[14].equals("1"))
			return "Entertainment";
		if(articleMetaData[15].equals("1"))
			return "Business";
		if(articleMetaData[16].equals("1"))
			return "Social Media";
		if(articleMetaData[17].equals("1"))
			return "Tech";
		if(articleMetaData[18].equals("1"))
			return "World";
		
		return "";
	}


	@POST
	@Path("predict")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces(MediaType.APPLICATION_JSON)
	public String predictPopularity(Article article) throws Exception{
		
		Map<String,String> map = new HashMap<>();
		
		map.put("titleName",article.getTitle());
		map.put("linksNumber",article.getLinksNumber().toString());
		map.put("imagesNumber",article.getImagesNumber().toString());
		map.put("videosNumber",article.getVideosNumber().toString());
		map.put("keywords", article.getKeywords().toString());
		map.put("articleContent", article.getArticleContent());
		map.put("day", article.getDay());
		map.put("category", article.getCategory());
		
		HttpClient client = HttpClientBuilder.create().build();
		String url = "http://localhost:9999/_ah/api/prediction/v1/prediction";
		HttpPost post = new HttpPost(url);
		
		StringEntity se = new StringEntity(new Gson().toJson(map));
		post.setEntity(se);
		post.setHeader("Content-type", "application/json");
		HttpResponse response = client.execute(post);
		HttpEntity entity = response.getEntity();
		
		String responseString = EntityUtils.toString(entity, "UTF-8");
		JsonObject learnerResponseJson = new JsonParser().parse(responseString).getAsJsonObject();
		
		String computedResponse = saveArticlesES();
		JsonObject computedResponseJson = new JsonParser().parse(computedResponse).getAsJsonObject();
		
		Set<Map.Entry<String, JsonElement>> entries = computedResponseJson.entrySet();
		
		for (Map.Entry<String, JsonElement> entry: entries) {
			learnerResponseJson.add(entry.getKey(), entry.getValue());
		}
		
		System.out.println(learnerResponseJson);
		
		return (learnerResponseJson.toString());
	}
	
}
