module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("assets");
  eleventyConfig.addPassthroughCopy("admin");
  return {
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site"
    }
  };
};