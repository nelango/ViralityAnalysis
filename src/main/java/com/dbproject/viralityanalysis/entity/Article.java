package com.dbproject.viralityanalysis.entity;


import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.google.appengine.repackaged.com.google.gson.Gson;
import com.googlecode.objectify.annotation.Entity;
import com.googlecode.objectify.annotation.Id;

/**
 * A class representing a User entity.
 */
@Entity
public class Article {

	private String titleName;
	private Long linksNumber;
	private Long imagesNumber;
	private Long videosNumber;
	private Long keywords;
	private String articleContent;
	private String day;
	private String category;

	@SuppressWarnings("unused")
	private Article() {
		this.articleContent = "";
		this.linksNumber = null;
		this.imagesNumber = null;
		this.videosNumber = null;
		this.keywords = null;
		this.day = "";
		this.category="";
		this.titleName = "";
	}

	@JsonCreator
	public Article(
			@JsonProperty("article") String articleContent,
			@JsonProperty("linksNumber") Long linksNumber,
			@JsonProperty("imagesNumber") Long imagesNumber,
			@JsonProperty("videosNumber") Long videosNumber,
			@JsonProperty("keywords") Long keywords,
			@JsonProperty("titleName") String titleName,
			@JsonProperty("day") String day,
			@JsonProperty("category") String category)
	{
		this.articleContent = articleContent;
		this.linksNumber = linksNumber;
		this.imagesNumber = imagesNumber;
		this.videosNumber = videosNumber;
		this.keywords = keywords;
		this.day=category;
		this.category=category;
		this.titleName = titleName;
	}

	public String getTitle()
	{
		return titleName;
	}

	public void setTitle(String title)
	{
		this.titleName = title;
	}

	/**
	 * @return the linksNumber
	 */
	public Long getLinksNumber() {
		return linksNumber;
	}

	/**
	 * @param linksNumber the linksNumber to set
	 */
	public void setLinksNumber(Long linksNumber) {
		this.linksNumber = linksNumber;
	}

	/**
	 * @return the imagesNumber
	 */
	public Long getImagesNumber() {
		return imagesNumber;
	}

	/**
	 * @param imagesNumber the imagesNumber to set
	 */
	public void setImagesNumber(Long imagesNumber) {
		this.imagesNumber = imagesNumber;
	}

	/**
	 * @return the videosNumber
	 */
	public Long getVideosNumber() {
		return videosNumber;
	}

	/**
	 * @param videosNumber the videosNumber to set
	 */
	public void setVideosNumber(Long videosNumber) {
		this.videosNumber = videosNumber;
	}

	/**
	 * @return the keywords
	 */
	public Long getKeywords() {
		return keywords;
	}

	/**
	 * @param keywords the keywords to set
	 */
	public void setKeywords(Long keywords) {
		this.keywords = keywords;
	}

	public String getArticleContent() {
		return articleContent;
	}

	/**
	 * @param articleContent the articleContent to set
	 */
	public void setArticleContent(String articleContent) {
		this.articleContent = articleContent;
	}

	public static String getJson(Article article)
	{
		String jsonRep = new Gson().toJson(article);
		return jsonRep;
	}

	/**
	 * @return the day
	 */
	public String getDay() {
		return day;
	}

	/**
	 * @param day the day to set
	 */
	public void setDay(String day) {
		this.day = day;
	}

	/**
	 * @return the category
	 */
	public String getCategory() {
		return category;
	}

	/**
	 * @param category the category to set
	 */
	public void setCategory(String category) {
		this.category = category;
	}

}
