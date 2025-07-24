# MongoDB Aggregation Queries for Anime Analytics

This file contains the MongoDB queries used for analysis tasks as described in the project.

---

## Task 1 – Studio Ghibli - Ratings by Year

```javascript
db.anime.aggregate([
  {
    $match: { Studio: "Studio Ghibli" }
  },
  {
    $project: {
      Rank: 1,
      Name: 1,
      Release_year: 1,
      Type: 1,
      Tags: 1,
      Rating: 1,
      Content_Warning: 1
    }
  },
  {
    $sort: { Release_year: 1 }
  }
]);
```

---