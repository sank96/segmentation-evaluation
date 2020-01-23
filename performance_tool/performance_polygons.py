from shapely.geometry import Polygon


class CorrectPolygon:
    def __init__(self, obj_dict: dict):
        pts = obj_dict['points']

        self.polygon: Polygon = Polygon(pts)
        self.used = False
        self.iou = None


class ToEvaluatePolygon:
    def __init__(self, obj_dict: dict):
        pts = obj_dict['points']

        self.polygon: Polygon = Polygon(pts)
        self.match = None
        self.used = False
        self.iou = None

    def compute_intersection_over_union(self, to_check: CorrectPolygon):
        pol_to_check = to_check.polygon
        intersection = self.polygon.intersection(pol_to_check).area
        union = self.polygon.union(pol_to_check).area
        print("intersection: ", intersection, " union: ", union)
        return intersection / union

    def find_best_iou(self, to_check_pols: [CorrectPolygon]):
        max_iou = (-1, None)
        for to_check_pol in to_check_pols:
            iou = self.compute_intersection_over_union(to_check_pol)

            print(iou)

            if iou > max_iou[0]:
                max_iou = (iou, to_check_pol)

        return max_iou

    def is_matched(self):
        if self.match is None:
            return False
        else:
            return True

    def get_count_match(self):
        if self.match is None:
            return 0
        else:
            return 1
