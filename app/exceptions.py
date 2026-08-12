class UniversityManagementError(Exception):
    pass


class StudentNotFoundError(UniversityManagementError):
    pass


class DuplicateStudentError(UniversityManagementError):
    pass


class ValidationError(UniversityManagementError):
    pass