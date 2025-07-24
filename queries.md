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

---

## Task 2 - User Ratings by Tag Count

```javascript
db.anime.aggregate([
  {
    $project: {
      Rank: 1,
      Rating: 1,
      Number_of_Tags: { $size: { $ifNull: ["$Tags", []] } }
    }
  },
  {
    $sort: { Rating: -1 }
  }
]);
```
---

## Task 3 - Most Popular Tags in Anime Productions

```javascript
db.anime.aggregate([
  {
    $unwind: "$Tags",
  },
  {
    $group: {
      _id: "$Tags",
      NumberOfProductions: { $sum: 1 }
    }
  },
  {
    $sort: { NumberOfProductions: -1 }
  },
  {
    $project: {
      _id: 0,
      Tag: "$_id",
      NumberOfProductions: 1
    }
  }
]);
```