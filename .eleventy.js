module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("admin");
  eleventyConfig.addPassthroughCopy("thanks.html");

  // Date filter for post listings
  eleventyConfig.addFilter("date", function(value, format) {
    if (!value) return "";
    var d = value instanceof Date ? value : new Date(value);
    if (isNaN(d.getTime())) return "";
    var months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
    var short = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    format = format || "MMMM d, yyyy";
    return format
      .replace("MMMM", months[d.getMonth()])
      .replace("MMM", short[d.getMonth()])
      .replace("yyyy", d.getFullYear())
      .replace("d", d.getDate());
  });

  // Posts collection
  eleventyConfig.addCollection("posts", function(collection) {
    return collection.getFilteredByGlob("posts/*.md").sort(function(a, b) {
      return a.date - b.date;
    });
  });

  return {
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site"
    }
  };
};
