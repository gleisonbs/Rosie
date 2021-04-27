from unittest import TestCase

from rosie.intent import Intent


class NLP:
    def __call__(self, obj):
        return self.Doc(obj)

    class Doc:
        def __init__(self, obj):
            self.obj = obj

        def __str__(self):
            return self.obj

        def similarity(self, dummy):
            return 0.5


class TestIntent(TestCase):
    def setUp(self):
        self.intent = Intent(NLP(), "test.intent")

    def tearDown(self):
        self.intent = None

    def test_has_all_attributes(self):
        self.assertEqual(
            hasattr(self.intent, "name"),
            True,
            "Intent: no name attribute found",
        )
        self.assertEqual(
            hasattr(self.intent, "phrases"),
            True,
            "Intent: no phrases attribute found",
        )
        self.assertEqual(
            hasattr(self.intent, "nlp_engine"),
            True,
            "Intent: no nlp_engine attribute found",
        )

    def test_can_initiate_correctly(self):
        self.assertEqual(
            self.intent.name,
            "test.intent",
            "Intent: name attribute initialized incorrectly",
        )
        self.assertEqual(
            self.intent.phrases,
            set(),
            "Intent: phrases attribute initialized incorrectly",
        )
        self.assertNotEqual(
            self.intent.nlp_engine,
            None,
            "Intent: nlp_engine attribute initialized incorrectly",
        )

    def test_has_get_similarity_method(self):
        self.assertEqual(
            hasattr(self.intent, "get_similarity"),
            True,
            "Intent: no get_similarity method found",
        )
        get_similarity = self.intent.get_similarity
        self.assertEqual(
            hasattr(get_similarity, "__call__"),
            True,
            "Intent: get_similarity is not a method",
        )
        self.assertEqual(
            get_similarity.__code__.co_argcount,
            1 + 1,
            "Intent: get_similarity should accept one parameter (token)",
        )

    def test_has_add_phrase_method(self):
        self.assertEqual(
            hasattr(self.intent, "add_phrase"),
            True,
            "Intent: no add_phrase method found",
        )
        add_phrase = self.intent.add_phrase
        self.assertEqual(
            hasattr(add_phrase, "__call__"),
            True,
            "Intent: add_phrase is not a method",
        )
        self.assertEqual(
            add_phrase.__code__.co_argcount,
            1 + 1,
            "Intent: add_phrase should accept one parameter (phrase)",
        )

    def test_correctly_adds_new_phrase(self):
        self.assertEqual(
            len(self.intent.phrases),
            0,
            "Intent: phrases should be empty when initialized",
        )
        self.intent.add_phrase("test.phrase")
        self.assertEqual(
            len(self.intent.phrases),
            1,
            "intent: add_phrase failed to add to phrases",
        )

    def test_correctly_returns_most_similar_intent(self):
        self.intent.add_phrase("qual o valor")
        self.intent.add_phrase("me fala o valor")
        self.intent.add_phrase("quanto custa")
        self.intent.add_phrase("quero saber o preço")
        self.intent.add_phrase("me fala o total")

        similarity = self.intent.get_similarity("qual o valor")
        self.assertNotEqual(similarity, 0)

        similarity = self.intent.get_similarity("qual o preço")
        self.assertGreater(similarity, 0)
        self.assertLessEqual(similarity, 1)

    def test_prints_correctly(self):
        self.assertEqual(
            str(self.intent), "intent:test.intent\n no phrases defined"
        )

        self.intent.add_phrase("test1")
        self.intent.add_phrase("test2")
        self.intent.add_phrase("test3")

        expected_str = """intent:test.intent
 - test1
 - test2
 - test3
"""
        self.assertEqual(
            str(self.intent),
            expected_str,
            "Intent: __str__ return incorrect formatted data",
        )
