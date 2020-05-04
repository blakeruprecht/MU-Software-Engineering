# Assignment 7: User Experience & Integration Focus (team) : Spring 2019 : CS4320/7320 Software Engineering


# __Option 1 (The Original Option)__
## You have new groups
In this exercise you familiarize yourself data served up at this set of API Endpoints, and design three visualizations. Use one of the strategies identified here to facilitate your visualization design process, which ideally you will perform **as a group**. 

https://toolkit.mozilla.org/methods/

### Endpoints to familiarize yourself with:  
1. http://czi2.osshealth.io:5153/api/unstable/  or this one: http://science.osshealth.io/ ... http://science.osshealth.io:5000/api/unstable/repo-groups .... and here is an endpoint with some data .... http://czi.osshealth.io:5150/api/unstable/repo-groups/332/repos/26139/lines-changed-by-author  
2. Kubernetes Dashboard: https://k8s.devstats.cncf.io/d/12/dashboards?orgId=1&from=now-7d&to=now-1h&refresh=15m 
2. The specific endpoints available are documented here: http://augur.osshealth.io/api_docs/
3. Your end product must be web deployable **in the next assignment***, and you can use any framework that allows you to call data from an API. Here is one example: https://twitter.github.io/year-in-review 
4. The source for the Twitter year in review site is here: https://github.com/sgoggins/twitter.github.io
5. There is a more complex and integrated strategy in the Augur project you have already cloned. 
6. You can pull data and build a mockup with one page. It does not have to be highly functional. 
7. Use these resources to organize 
8. **TURN IN** a JSON file of the data you want to visualize, **AND** your three visualization designs in a folder in one repository of one team member. There should be three different visualization designs, and three different JSON files. 

## Endpoints to look at: 
1. http://czi2.osshealth.io:5153/api/unstable/repos : repo list
2. http://czi2.osshealth.io:5153/api/unstable/repo-groups : repo group list 
3. http://czi2.osshealth.io:5153/api/unstable/repo-groups/25182/repos/27857/reviews : List of pull requests for a particular repo and repo group
4. http://czi2.osshealth.io:5153/api/unstable/repo-groups/99999/repos/27857/reviews : Same list of pull requests for a particular repo, but illustrating how the API is a bit flawed and ignores the repo-group when given a repo_id because all repo_id's are unique
5. **note** A "Review" is the CHAOSS word for "Pull Request". 
  - Reviews: https://chaoss.community/metric-reviews/
  - Reviews Accepted https://chaoss.community/metric-reviews-accepted/ (chaoss metric)


# __Option 2 (Alternative Option)__
1. Find a set of endpoints
2. You can pull data and build a mockup with one page. It does not have to be highly functional. 
3. Use these resources to organize 
4. **TURN IN** a JSON file of the data you want to visualize, **AND** your three visualization designs in a folder in one repository of one team member. There should be three different visualization designs, and three different JSON files. 

