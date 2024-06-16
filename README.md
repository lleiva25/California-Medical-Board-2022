![image](https://github.com/lleiva25/California-Medical-Board-2022/assets/140974405/6041abd6-155e-4b9b-8a77-ebd15e909801)
# California Medical Board 2022
-------------------------------------------------------------------------------------------------
Mission
-------------------------------------------------------------------------------------------------
The mission of the Medical Board of California is to protect healthcare consumers and prevent harm through the proper licensing and regulation of physicians and surgeons and certain allied healthcare professionals and through the vigorous, objective enforcement of the Medical Practice Act, and to promote access to quality medical care through the Board's licensing, policy, and regulatory functions.

-------------------------------------------------------------------------------------------------
Dashboard
-------------------------------------------------------------------------------------------------
Dashboard Link: https://california-medical-board-2022.onrender.com

![06_County_Alerts_Geo](https://github.com/lleiva25/California-Medical-Board-2022/assets/140974405/13a94830-be02-4281-83ce-b35e57b2eb75)
![07_Disciplinary_Action_Pie](https://github.com/lleiva25/California-Medical-Board-2022/assets/140974405/f17ac0bf-7d7d-45fc-958f-b52b1a7eff4c)
![01_No_Medical_School_Bar](https://github.com/lleiva25/California-Medical-Board-2022/assets/140974405/be565682-c981-442b-98ee-1f651516607d)

-------------------------------------------------------------------------------------------------
Modules Utilized
-------------------------------------------------------------------------------------------------
| Dependencies | Abbr | Decscription |
|-------|------------|------------|
| Pandas | pd | Fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.|
| sqlite3 | | C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. |
| Datetime | dt | Module supplies classes for manipulating dates and times.|
| Matplotlib.pyplot | plt | Comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.|
| Shapely.geometry | | Shapely geometry classes, such as shapely.Point, are the central data types in Shapely. Each geometry class extends the shapely.Geometry base class, which is a container of the underlying GEOS geometry object, to provide geometry type-specific attributes and behavior.|
| Shapefile | shp | The Shapefile C Library provides the ability to write simple C programs for reading, writing and updating (to a limited extent) ESRI Shapefiles, and the associated attribute file (.dbf).|
| Plotly| | Put data and AI into action with scalable, interactive data apps for your organization.|
| Numpy | np | A library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.|
| Requests| | Requests is an HTTP client library for the Python programming language. Requests is one of the most downloaded Python libraries, with over 300 million monthly downloads. It maps the HTTP protocol onto Python's object-oriented semantics. |
| Warnings| | Temporarily Suppressing Warnings |
| Reduce (Functools) | | For higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.|

-------------------------------------------------------------------------------------------------
Data Process
-------------------------------------------------------------------------------------------------
1. Filter data to the year "2022".
2. Convert date category to Datetime.
3. Rename columns.
4. Drop irrelevant columns.
5. Utilize groupby attribute to show counts and sums in table.
6. Reset index then save to .JSON or .CSV for app development
   
-------------------------------------------------------------------------------------------------
Definitions
-------------------------------------------------------------------------------------------------
| Term | Decscription |
|-------|------------|
| Disciplinary Alert | Some form of official and documented action to sanction unwanted behavior. |
| Fraud| Deceit, trickery, sharp practice, or breach of confidence, perpetrated for profit or to gain some unfair or dishonest advantage |
| Sexual Offense| Any crime that involves sexual intercourse or any other sexual act|
| Receiving Kickback | To a misappropriation of funds that enriches a person of power or influence who uses the power or influence to make a different individual, organization, or company richer |
| Tax Evasion | The illegal non-payment or under-payment of taxes, usually by deliberately making a false declaration or no declaration to tax authorities|
| Illegal Imports| Importing restricted or prohibited goods|
| Conspiracy | Plot, ploy, or scheme, is a secret plan or agreement between people (called conspirers or conspirators) for an unlawful or harmful purpose, such as murder, treason, or corruption, especially with a political motivation, while keeping their agreement secret from the public or from other people affected by it. |

-------------------------------------------------------------------------------------------------
License Explanation
-------------------------------------------------------------------------------------------------
| Type | Decscription |
| ------------- | ------------- |
|A  | Licensee is a U.S. or Canadian medical school graduate whose pathway to licensure was based on: 1) The FLEX, USMLE, or LMCC written examination and has been licensed less than four years in another state, OR 2) An international medical school graduate whose pathway to licensure was based on the above exams or approved combinations of the NBME, FLEX, and USMLE.|
|C  | Licensee is a U.S., Canadian, or international medical school graduate whose pathway to licensure was based on licensure in another state for four or more years. Additionally, international graduates may also be subject to the C-SPEX examination.|
|G  | Licensee is a U.S. or Canadian medical school graduate whose pathway to licensure was based on the NBME examination.|

-------------------------------------------------------------------------------------------------
List of Convictions
-------------------------------------------------------------------------------------------------
| Conviction | Decscription |
| ------------- | ------------- |
| Probation | A prison sentence that is suspended on the condition that the offender follow certain prescribed rules and commit no further crimes |
| Public Reprimand | Issued by the Licensing Program to an applicant for a minor violation that does not require probationary status or warrant denial of the license |
| Surrender of License | The court suspends the privilege of a person to operate with license, the court shall require the person's license to be surrendered to it.|
| Revoked | The court takes a physcician's license, either for a period of time or permanently.|
| Accusation Filed | An accusation is the document containing charges and allegations, that is filed when an agency is seeking to discipline a licensee.|
