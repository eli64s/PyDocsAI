"""
Tests for the readme-ai package.
"""

from unittest.mock import patch

import pytest

from readmeai.__main__ import readme_agent, readme_generator
from readmeai._exceptions import ReadmeGeneratorError


@patch("readmeai.__main__.retrieve_repository")
@patch("readmeai.__main__.preprocessor")
@patch("readmeai.__main__.ModelRegistry.get_backend")
@patch("readmeai.__main__.MarkdownBuilder.build")
@pytest.mark.asyncio
async def test_readme_generator(
    mock_build_markdown,
    mock_get_backend,
    mock_preprocessor,
    mock_retrieve_repository,
    mock_config,
    mock_configs,
    mock_dependencies,
    mock_summaries,
    tmp_path,
):
    """Test the readme_generator function."""
    mock_retrieve_repository.return_value = tmp_path
    mock_preprocessor.return_value = (
        mock_dependencies,
        mock_summaries,
        # {"dependency1": "command1", "dependency2": "command2"},
    )
    mock_config.git.repository = tmp_path
    mock_get_backend.return_value.use_api.return_value.__aenter__.return_value.batch_request.return_value = (
        "summaries_response",
        "features_response",
        "overview_response",
        "slogan_response",
    )
    mock_output_file = str(tmp_path / "test_readme.md")
    mock_build_markdown.return_value = mock_output_file
    await readme_generator(mock_configs, mock_output_file)
    mock_retrieve_repository.assert_called_once()
    mock_preprocessor.assert_called_once()
    mock_get_backend.assert_called_once()
    mock_build_markdown.assert_called_once()


@pytest.mark.asyncio
async def test_readme_agent_exception_handling():
    """Test the readme_agent function exception handling."""
    with (
        patch(
            "readmeai.__main__.readme_agent",
            side_effect=Exception("Test exception"),
        ),
        pytest.raises(ReadmeGeneratorError) as exc,
    ):
        readme_agent(
            align=None,
            api="invalid_api_provider",
            badge_style=None,
            badge_color=None,
            base_url=None,
            context_window=None,
            emojis=None,
            header_style=None,
            image=None,
            model=None,
            output="test_output.md",
            rate_limit=None,
            repository="https:///invalid_url",
            temperature=None,
            tree_depth=None,
            toc_style="bullets",
            top_p=None,
        )
    assert isinstance(exc.value, ReadmeGeneratorError)


@pytest.mark.asyncio
async def test_readme_generator_exception_handling():
    """Test the readme_generator function exception handling."""
    with pytest.raises(Exception) as exc:
        await readme_generator({}, "test_output.md")
    assert isinstance(exc.value, Exception)
