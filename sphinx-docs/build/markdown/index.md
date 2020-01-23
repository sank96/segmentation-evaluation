<!-- Segmentation Evaluation Tool documentation master file, created by
sphinx-quickstart on Thu Jan 23 18:22:06 2020.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Segmentation Evaluation Tool

## Manually Segmentation

The module gives all the functions used through the manually segmentation


### performance_tool.manually_segmentation.get_image(original: bool = False)
The function return the image on which print the objects. If original is not provided the objects already segmented
are shown in light gray color.


* **Parameters**

    **original** (*bool*) – The parameter specify when return the original image of the image with the already insert polygons.



* **Returns**

    The image required is return



### performance_tool.manually_segmentation.manually_segmentation()
The function asks the path of the image to segment and the folder in which saves the output json.

The output is a JSON structure in a dictionary. The key is an integer that represent uniquely the object segmented.
Each value are the vertices of the polygon used to segment the object.


* **Returns**

    A bool value that check if all operations end correctly



* **Return type**

    bool



### performance_tool.manually_segmentation.plot_all_polygons(pols: [<class 'dict'>], final=False)
The function plot all polygons into the image. If the function is called as final version the image is not shown,
otherwise it is printed into a window.


* **Parameters**

    
    * **pols** (*list*) – A list containing all the polygon represented as a dictionary


    * **final** (*bool*) – Parameter that represent when print the image and return or only return



* **Returns**

    Return the image on which all the polygons are printed



### performance_tool.manually_segmentation.plot_shape(saving: bool = False)
The function takes care of print the points, line and polygons while the selection


* **Parameters**

    **saving** (*bool*) – The parameters represent when print the polygons in saving mode (in red colors instead of green).



### performance_tool.manually_segmentation.shape_selection(event, x, y, flags, param)
The method is called when the required event is listen through openCV


* **Parameters**

    
    * **event** – Name of the event


    * **x** – Position x of the event


    * **y** – Position y of the event


    * **flags** – Not used parameter


    * **param** – Not used parametr


## Evaluate Segmentation

The package contains all the functions used to evaluate the segmentation


### performance_tool.evaluate_segmentation.claster_on_label(data: dict, correct: bool)
Given the dictionary with all the polygons serialized return another dictionary in which keys are the distinct
labels of the input data.
The value of each key is a list of polygon object. They are two different object depends on the input data collects
the correct objects or objects to evaluate.


* **Parameters**

    
    * **data** (*dict*) – The dictionary contains all polygons serialized


    * **correct** (*bool*) – The value that represent if the input data are the correct polygons or polygons to check



* **Returns**

    Polygons clustered on the label name. Dictionary with keys distinct labels



* **Return type**

    dict



### performance_tool.evaluate_segmentation.evaluate_segmentation()
The function ask for the two json file to match.

The structure of the JSON must be a dictionary as key an increment number that represent uniquely an object.
The value is another dictionary with two key *label* (the name of the template) and *points* (a list of float).


* **Returns**

    A bool value that check if all operations end correctly



* **Return type**

    bool


## Data Structure for evaluation

The package contains the data structures used to perform the evaluation


### class performance_tool.performance_polygons.CorrectPolygon(obj_dict: dict)
The class represents a polygon reads from the file of the ground truth


### class performance_tool.performance_polygons.ToEvaluatePolygon(obj_dict: dict)
The class represents a polygon segmented by an algorithm that must be evaluated


#### compute_intersection_over_union(to_check: performance_tool.performance_polygons.CorrectPolygon)
Given a correct polygon the method perform the intersection over the union.


* **Parameters**

    **to_check** (*CorrectPolygon*) – the correct polygon with which check the correctness of the evaluating polygon



* **Returns**

    The intersection over the union



* **Return type**

    float



#### find_best_iou(to_check_pols: [<class 'performance_tool.performance_polygons.CorrectPolygon'>])
The method return the best intersection over the union computed with several correct polygons.


* **Parameters**

    **to_check_pols** (*list*) – List of correct polygons with which compute IOU and find the best



* **Returns**

    Return a tuple corresponding to the value of the best intersection over the union and the correct polygon with which it is calculated



* **Return type**

    tuple



#### get_count_match()
Return the addend of the summation


* **Returns**

    0 if the object is not matched, 1 otherwise



* **Return type**

    int



#### is_matched()
Check the self object has already checked


* **Returns**

    Boolean value



* **Return type**

    bool
