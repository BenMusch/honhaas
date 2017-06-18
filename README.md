# Hotdog or Not Hotdog as as Service

Note: `output_graph.pb` was too large to put on GitHub. You'll have to train the
data to run this locally.


API:

```javascript
// POST: /is_hotdog?image={image url}

// RESPONSE:

// 200 SUCCESS:

{
  is_hotdog: Boolean /* prediction of whether or not it is a hotdog */
  scores: [
    String,          /* Category name */
    Float,           /* Score (0.0 <= score <= 1.0) */
  ]
}

// 500 ERROR:

{
  error: String /* Error message */
}
```



Major thanks to these talks for teaching me this stuff:

https://www.youtube.com/watch?v=8G709hKkthY

https://www.youtube.com/watch?v=Q9Z20HCPnww

https://www.youtube.com/watch?v=S4vL355capU&t=415s

And this repo:

https://github.com/kmather73/NotHotdog-Classifier
