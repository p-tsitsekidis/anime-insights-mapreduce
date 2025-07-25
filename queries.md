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

---

---

## Task 4 –  Studio Average Ratings vs. Average Episode Count

```javascript
db.anime.aggregate([
  {
    $group: {
      _id: "$Studio",
      Avg_Episodes: {
        $avg: "$Episodes"
      },
      Avg_Rating: {
        $avg: "$Rating",
      }
    },
    $sort: {
      Avg_Rating: -1
    }
  }
]);
```

---

---

## Task 5 – Designer Analysis

```javascript
db.anime.aggregate([
  {
    $match: {
      "staff.Character Design": { $exists: true }
    }
  },
  {
    $group: {
      _id: {
        designer: "$staff.Character Design",
        studio: "$Studio"
      },
      avgRating: { $avg: "$Rating" },
      productions: { $sum: 1 }
    }
  },
  {
    $group: {
      _id: "$_id.designer",
      studios: {
        $push: {
          studio: "$_id.studio",
          avgRating: "$avgRating",
          productions: "$productions"
        }
      },
      totalProductions: { $sum: "$productions" }
    }
  },
  {
    $project: {
      _id: 0,
      designer: "$_id",
      totalProductions: 1,
      studios: 1
    }
  },
  {
    $sort: {
      totalProductions: -1
    }
  }
])
```

---

---

## Task 6 – Franchise Analysis

```javascript
db.anime.aggregate([
  {
    $addFields: {
      franchise: "$Related_anime"
    }
  },
  {
    $unwind: "$franchise"
  },
  {
    $group: {
      _id: "$franchise",
      numberOfAnime: { $sum: 1 },
      averageEpisodes: { $avg: "$Episodes" },
      releasePeriodStart: { $min: "$Release_year" },
      releasePeriodEnd: { $max: "$End_year" },
      averageRating: { $avg: "$Rating" }
    }
  },
  {
    $sort: {
      numberOfAnime: -1
    }
  }
])
```

---