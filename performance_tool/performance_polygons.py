"""
The package contains the data structures used to perform the evaluation
"""
from shapely.geometry import Polygon


class CorrectPolygon:
    """
    The class represents a polygon reads from the file of the ground truth
    """
    def __init__(self, obj_dict: dict):
        pts = obj_dict['points']

        self.polygon: Polygon = Polygon(pts)
        self.used = False
        self.iou = None


class ToEvaluatePolygon:
    """
    The class represents a polygon segmented by an algorithm that must be evaluated
    """
    def __init__(self, obj_dict: dict):
        pts = obj_dict['points']

        self.polygon: Polygon = Polygon(pts)
        self.match = None
        self.used = False
        self.iou = None

    def compute_intersection_over_union(self, to_check: CorrectPolygon) -> float:
        """
        Given a correct polygon the method perform the intersection over the union.

        :param to_check: the correct polygon with which check the correctness of the evaluating polygon
        :type to_check: CorrectPolygon
        :return: The intersection over the union
        :rtype: float
        """
        pol_to_check = to_check.polygon
        intersection = self.polygon.intersection(pol_to_check).area
        union = self.polygon.union(pol_to_check).area
        # print("intersection: ", intersection, " union: ", union)
        return intersection / union

    def find_best_iou(self, to_check_pols: [CorrectPolygon]) -> tuple:
        """
        The method return the best intersection over the union computed with several correct polygons.

        :param to_check_pols: List of correct polygons with which compute IOU and find the best
        :type to_check_pols: list
        :return: Return a tuple corresponding to the value of the best intersection over the union and the correct polygon with which it is calculated
        :rtype: tuple
        """
        max_iou = (-1, None)
        for to_check_pol in to_check_pols:
            iou = self.compute_intersection_over_union(to_check_pol)

            # print(iou)

            if iou > max_iou[0]:
                max_iou = (iou, to_check_pol)

        return max_iou

    def is_matched(self) -> bool:
        """
        Check the self object has already checked

        :return: Boolean value
        :rtype: bool
        """
        if self.match is None:
            return False
        else:
            return True

    def get_count_match(self) -> int:
        """
        Return the addend of the summation

        :return: 0 if the object is not matched, 1 otherwise
        :rtype: int
        """
        if self.match is None:
            return 0
        else:
            return 1
